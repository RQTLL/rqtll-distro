from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Optional

from PySide6.QtCore import QPointF, QRectF, Qt, Signal, QObject
from PySide6.QtGui import QColor, QFont, QFontMetrics, QPainter, QPainterPath, QPen
from PySide6.QtWidgets import QGraphicsItem, QGraphicsObject, QGraphicsPathItem, QGraphicsScene, QGraphicsView


@dataclass
class NodeModel:
    id: str = field(default_factory=lambda: uuid.uuid4().hex)
    name: str = ""
    type_: str = ""
    pos: List[float] = field(default_factory=lambda: [0.0, 0.0])
    properties: Dict[str, object] = field(default_factory=dict)
    custom_properties: Dict[str, object] = field(default_factory=dict)

    def set_property(self, name: str, value):
        self.properties[name] = value
        self.custom_properties[name] = value
        if name == "pos":
            self.pos = [float(value[0]), float(value[1])]
        elif name == "name":
            self.name = value
        else:
            setattr(self, name, value)


class Port:
    def __init__(self, node: "BaseNode", name: str, is_output: bool, multi_connection: bool = False):
        self._node = node
        self._name = name
        self._is_output = is_output
        self._multi_connection = multi_connection
        self._connections: List[ConnectionItem] = []

    def node(self):
        return self._node

    def name(self):
        return self._name

    def type_(self):
        return "out" if self._is_output else "in"

    def multi_connection(self):
        return self._multi_connection

    def connected_ports(self):
        return [conn.target_port if conn.source_port is self else conn.source_port for conn in self._connections]

    def connect_to(self, port=None, push_undo=True, emit_signal=True):
        if port is None or port is self:
            return

        if self.type_() == port.type_():
            return

        source = self if self.type_() == "out" else port
        target = port if source is self else self

        graph = source.node().graph
        if graph is None or graph is not target.node().graph:
            return

        for connection in self._connections:
            if connection.source_port is source and connection.target_port is target:
                return

        if not source.multi_connection() and source._connections:
            return
        if not target.multi_connection() and target._connections:
            return

        connection = ConnectionItem(source, target)
        graph._register_connection(connection)


class NodeItem(QGraphicsObject):
    def __init__(self, node: "BaseNode"):
        super().__init__()
        self.node = node
        self.id = node.id
        self.name = node.model.name
        self.xy_pos = [0.0, 0.0]
        self.width = 160.0
        self.height = 120.0
        self._color = QColor(50, 56, 64)
        self._border_color = QColor(86, 104, 128)
        self._text_color = QColor(242, 246, 255)
        self._previous_pos = QPointF(0.0, 0.0)
        self._suppress_move_signal = False
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemSendsGeometryChanges, True)
        self.setCacheMode(QGraphicsItem.CacheMode.DeviceCoordinateCache)

    def boundingRect(self):
        return QRectF(0.0, 0.0, float(self.width), float(self.height))

    def paint(self, painter, option, widget=None):
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        rect = self.boundingRect()
        radius = 8.0

        is_dark = True
        if self.node.graph and hasattr(self.node.graph, "theme_name"):
            is_dark = (self.node.graph.theme_name == "dark")

        body_color = QColor(43, 43, 43) if is_dark else QColor(230, 230, 230)
        
        if self.isSelected():
            border_pen = QPen(QColor(241, 155, 60) if is_dark else QColor(0, 144, 255), 2.0)
        else:
            border_pen = QPen(self._border_color, 1.0)

        body_path = QPainterPath()
        body_path.addRoundedRect(rect.adjusted(0.5, 0.5, -0.5, -0.5), radius, radius)
        painter.setPen(border_pen)
        painter.setBrush(body_color)
        painter.drawPath(body_path)

        title_lines = str(self.name or self.node.model.name or "").splitlines() or [""]
        header_title = title_lines[0]

        font = QFont(painter.font())
        font.setPointSizeF(max(9.0, font.pointSizeF()))
        font.setBold(True)
        painter.setFont(font)
        metrics = QFontMetrics(font)
        
        header_height = 12 + metrics.height() + 6

        painter.save()
        painter.setClipPath(body_path)
        header_rect = QRectF(0.0, 0.0, rect.width(), header_height)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(self._color)
        painter.drawRect(header_rect)
        painter.restore()

        painter.setPen(QPen(QColor(60, 60, 60) if is_dark else QColor(200, 200, 200), 1.0))
        painter.drawLine(QPointF(0.5, header_height), QPointF(rect.width() - 0.5, header_height))

        painter.setPen(self._text_color)
        left_margin = 12
        right_margin = 12
        text_width = int(max(10.0, rect.width() - left_margin - right_margin))
        painter.drawText(
            QRectF(left_margin, 10, text_width, metrics.height()),
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter | Qt.TextFlag.TextSingleLine,
            header_title,
        )

        body_lines = title_lines[1:]
        if body_lines:
            painter.setFont(QFont(painter.font().family(), max(8, painter.font().pointSize() - 1)))
            painter.setPen(QColor(180, 190, 205) if is_dark else QColor(60, 60, 60))
            body_metrics = QFontMetrics(painter.font())
            body_y = header_height + 8
            for line in body_lines:
                painter.drawText(
                    QRectF(left_margin, body_y, text_width, body_metrics.height()),
                    Qt.AlignmentFlag.AlignCenter,
                    line,
                )
                body_y += body_metrics.lineSpacing()

        self._draw_ports(painter)

    def _shorten_port_name(self, name):
        if name in {"publishers", "subscribers"}:
            return name
        if len(name) <= 18:
            return name
        base = name.split("/")[-1]
        if len(base) > 15:
            return ".." + base[-13:]
        return ".." + base

    def _draw_ports(self, painter):
        port_radius = 4.0
        port_y = self._port_positions()
        
        font = QFont(painter.font())
        font.setPointSize(8)
        font.setBold(False)
        painter.setFont(font)
        metrics = QFontMetrics(font)
        
        is_dark = True
        if self.node.graph and hasattr(self.node.graph, "theme_name"):
            is_dark = (self.node.graph.theme_name == "dark")
        text_color = QColor(190, 200, 215) if is_dark else QColor(60, 60, 60)
        painter.setPen(text_color)
        
        painter.setBrush(QColor(255, 187, 0))

        for y, port in port_y["inputs"]:
            painter.drawEllipse(QPointF(0.0, y), port_radius, port_radius)
            display_name = self._shorten_port_name(port.name())
            text_rect = QRectF(8.0, y - metrics.height() / 2, self.width * 0.45, metrics.height())
            painter.drawText(text_rect, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter, display_name)

        for y, port in port_y["outputs"]:
            painter.drawEllipse(QPointF(self.width, y), port_radius, port_radius)
            display_name = self._shorten_port_name(port.name())
            text_rect = QRectF(self.width * 0.55 - 8.0, y - metrics.height() / 2, self.width * 0.45, metrics.height())
            painter.drawText(text_rect, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter, display_name)

    def port_scene_pos(self, port):
        port_positions = self._port_positions()
        for y, candidate in port_positions["inputs"]:
            if candidate is port:
                return self.mapToScene(QPointF(0.0, y))
        for y, candidate in port_positions["outputs"]:
            if candidate is port:
                return self.mapToScene(QPointF(self.width, y))
        return self.mapToScene(QPointF(self.width * 0.5, self.height * 0.5))

    def _port_positions(self):
        inputs = list(getattr(self.node, "_inputs", []))
        outputs = list(getattr(self.node, "_outputs", []))
        top = 48.0
        usable = max(24.0, self.height - top - 16.0)
        input_step = usable / max(1, len(inputs))
        output_step = usable / max(1, len(outputs))
        input_positions = []
        output_positions = []

        for index, port in enumerate(inputs):
            input_positions.append((top + (index + 0.5) * input_step, port))
        for index, port in enumerate(outputs):
            output_positions.append((top + (index + 0.5) * output_step, port))
        return {"inputs": input_positions, "outputs": output_positions}

    def set_display_name(self, name):
        self.name = name
        self._update_geometry()
        self.update()

    def set_color(self, color):
        self._color = color
        self.update()

    def set_text_color(self, color):
        self._text_color = color
        self.update()

    def _update_geometry(self):
        font = QFont()
        font.setPointSize(10)
        metrics = QFontMetrics(font)
        lines = max(1, len(str(self.name or self.node.model.name or "").splitlines()))
        longest_line = max((metrics.horizontalAdvance(line) for line in str(self.name or self.node.model.name or "").splitlines()), default=0)
        port_count = max(len(self.node._inputs), len(self.node._outputs), 1)
        self.prepareGeometryChange()
        self.width = max(260.0, float(longest_line + 52))
        self.height = max(96.0, float(52 + (lines * metrics.lineSpacing()) + (port_count * 16)))

    def set_node_pos(self, x, y):
        self._suppress_move_signal = True
        try:
            super().setPos(float(x), float(y))
        finally:
            self._suppress_move_signal = False
        self.xy_pos = [float(x), float(y)]

    def itemChange(self, change, value):
        if change == QGraphicsItem.GraphicsItemChange.ItemPositionChange:
            self._previous_pos = self.pos()
        elif change == QGraphicsItem.GraphicsItemChange.ItemPositionHasChanged:
            self.xy_pos = [float(value.x()), float(value.y())]
            self.node.model.pos = self.xy_pos[:]
            if not self._suppress_move_signal and self.node.graph is not None:
                self.node.graph._on_node_view_moved(self, self._previous_pos)
        return super().itemChange(change, value)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if event.button() == Qt.MouseButton.LeftButton and self.node.graph is not None:
            self.node.graph.node_selected.emit(self.node)


class ConnectionItem(QGraphicsPathItem):
    def __init__(self, source_port: Port, target_port: Port):
        super().__init__()
        self.source_port = source_port
        self.target_port = target_port
        self.setZValue(-1)
        self.setPen(QPen(QColor(120, 168, 255), 2.0, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
        self.update_path()
        source_port._connections.append(self)
        target_port._connections.append(self)

    def update_path(self):
        start = self.source_port.node().view.port_scene_pos(self.source_port)
        end = self.target_port.node().view.port_scene_pos(self.target_port)
        path = QPainterPath(start)
        dx = max(60.0, abs(end.x() - start.x()) * 0.5)
        control1 = QPointF(start.x() + dx, start.y())
        control2 = QPointF(end.x() - dx, end.y())
        path.cubicTo(control1, control2, end)
        self.setPath(path)


class NodeGraphViewer(QGraphicsView):
    moved_nodes = Signal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setScene(QGraphicsScene(self))
        self.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        self.setRenderHint(QPainter.RenderHint.TextAntialiasing, True)
        self.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.BoundingRectViewportUpdate)
        self.setDragMode(QGraphicsView.DragMode.RubberBandDrag)
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorViewCenter)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setFrameShape(QGraphicsView.Shape.NoFrame)
        self.setStyleSheet("background: transparent;")
        self._pan_start = None

    def wheelEvent(self, event):
        zoom_in_factor = 1.25
        zoom_out_factor = 0.8
        
        old_pos = self.mapToScene(event.position().toPoint() if hasattr(event, "position") else event.pos())
        
        if event.angleDelta().y() > 0:
            self.scale(zoom_in_factor, zoom_in_factor)
        else:
            self.scale(zoom_out_factor, zoom_out_factor)
            
        new_pos = self.mapToScene(event.position().toPoint() if hasattr(event, "position") else event.pos())
        
        delta = old_pos - new_pos
        self.translate(-delta.x(), -delta.y())

    def mousePressEvent(self, event):
        if event.button() in (Qt.MouseButton.RightButton, Qt.MouseButton.MiddleButton):
            self._pan_start = event.pos()
            self.setCursor(Qt.CursorShape.ClosedHandCursor)
            event.accept()
        else:
            super().mousePressEvent(event)
            
    def mouseReleaseEvent(self, event):
        if event.button() in (Qt.MouseButton.RightButton, Qt.MouseButton.MiddleButton):
            self._pan_start = None
            self.setCursor(Qt.CursorShape.ArrowCursor)
            event.accept()
        else:
            super().mouseReleaseEvent(event)
            
    def mouseMoveEvent(self, event):
        if hasattr(self, "_pan_start") and self._pan_start is not None:
            delta = event.pos() - self._pan_start
            self._pan_start = event.pos()
            
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - delta.x())
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() - delta.y())
            event.accept()
        else:
            super().mouseMoveEvent(event)


class BaseNode:
    __identifier__ = "nodegraphpyside.nodes"
    NODE_NAME = "Node"
    type_ = None

    def __init__(self):
        self._graph: Optional[NodeGraph] = None
        self.model = NodeModel()
        self.model.type_ = self.type_
        self.model.name = self.NODE_NAME or self.__class__.__name__
        self._inputs: List[Port] = []
        self._outputs: List[Port] = []
        self.color = QColor(50, 56, 64)
        self.text_color = QColor(242, 246, 255)
        self.view = NodeItem(self)

    @property
    def id(self):
        return self.model.id

    @property
    def graph(self):
        return self._graph

    def set_graph(self, graph):
        self._graph = graph

    def set_color(self, r, g, b, a=255):
        self.color = QColor(r, g, b, a)
        self.view.set_color(self.color)

    def create_property(self, name, value):
        self.model.set_property(name, value)

    def set_name(self, name):
        self.model.name = name
        self.model.set_property("name", name)
        self.view.set_display_name(name)

    def name(self):
        return self.model.name

    def add_input(self, name, multi_input=False):
        port = Port(self, name, is_output=False, multi_connection=multi_input)
        self._inputs.append(port)
        self.view._update_geometry()
        self.view.update()
        return port

    def add_output(self, name, multi_output=False):
        port = Port(self, name, is_output=True, multi_connection=multi_output)
        self._outputs.append(port)
        self.view._update_geometry()
        self.view.update()
        return port

    def inputs(self):
        return {port.name(): port for port in self._inputs}

    def outputs(self):
        return {port.name(): port for port in self._outputs}

    def set_pos(self, x, y):
        self.model.set_property("pos", [float(x), float(y)])
        self.view.set_node_pos(x, y)
        if self._graph is not None:
            self._graph._update_connections_for_node(self)

    def pos(self):
        return self.model.pos

    def x_pos(self):
        return self.model.pos[0]

    def y_pos(self):
        return self.model.pos[1]


class NodeGraph(QObject):
    node_selected = Signal(object)
    node_created = Signal(object)
    nodes_deleted = Signal(list)

    def __init__(self):
        super().__init__()
        self.theme_name = "dark"
        self._scene = QGraphicsScene()
        self._scene.setSceneRect(-10000.0, -10000.0, 20000.0, 20000.0)
        self._viewer = NodeGraphViewer()
        self._viewer.setScene(self._scene)
        self._viewer.moved_nodes.connect(self._on_nodes_moved)
        self.widget = self._viewer
        self._node_types: Dict[str, type] = {}
        self._nodes: Dict[str, BaseNode] = {}
        self._connections: List[ConnectionItem] = []

    def register_nodes(self, node_classes: Iterable[type]):
        for node_class in node_classes:
            type_name = f"{node_class.__identifier__}.{node_class.__name__}"
            node_class.type_ = type_name
            self._node_types[type_name] = node_class

    def create_node(self, type_, name=None, selected=False, color=None, text_color=None):
        node_class = self._node_types.get(type_)
        if node_class is None:
            raise KeyError(type_)
        node = node_class()
        node.set_graph(self)
        self._scene.addItem(node.view)
        self._nodes[node.id] = node
        if name is not None:
            node.set_name(name)
        if color is not None:
            if isinstance(color, str):
                node.view.set_color(QColor(color))
            else:
                node.view.set_color(QColor(color))
        if text_color is not None:
            node.view.set_text_color(QColor(text_color))
        if selected:
            node.view.setSelected(True)
        return node

    def clear_session(self):
        for connection in list(self._connections):
            self._scene.removeItem(connection)
        self._connections.clear()
        for node in list(self._nodes.values()):
            self._scene.removeItem(node.view)
        self._nodes.clear()

    def get_node_by_id(self, node_id):
        return self._nodes.get(node_id)

    def all_nodes(self):
        return list(self._nodes.values())

    def selected_nodes(self):
        return [node for node in self._nodes.values() if node.view.isSelected()]

    def viewer(self):
        return self._viewer

    def center_on(self, nodes=None, padding=120):
        nodes = list(nodes or self.all_nodes())
        if not nodes:
            return
        rect = None
        for node in nodes:
            node_rect = node.view.sceneBoundingRect()
            rect = node_rect if rect is None else rect.united(node_rect)
        if rect is None or rect.isNull():
            return
        rect = rect.adjusted(-padding, -padding, padding, padding)
        self._viewer.fitInView(rect, Qt.AspectRatioMode.KeepAspectRatio)

    def fit_to_selection(self, padding=120):
        self.center_on(self.selected_nodes(), padding=padding)

    def _register_connection(self, connection: ConnectionItem):
        self._connections.append(connection)
        self._scene.addItem(connection)
        self._update_connections_for_node(connection.source_port.node())
        self._update_connections_for_node(connection.target_port.node())

    def _update_connections_for_node(self, node):
        for port in node._inputs + node._outputs:
            for connection in port._connections:
                connection.update_path()

    def _on_nodes_moved(self, moved_nodes):
        for node_view, prev_pos in (moved_nodes or {}).items():
            node = self._nodes.get(getattr(node_view, "id", None))
            if node is None:
                continue
            node.model.pos = [float(node_view.xy_pos[0]), float(node_view.xy_pos[1])]
            self._update_connections_for_node(node)

    def _on_node_view_moved(self, node_view, prev_pos):
        self._viewer.moved_nodes.emit({node_view: prev_pos})


__all__ = ["BaseNode", "NodeGraph", "Port"]
