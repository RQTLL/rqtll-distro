use std::env;
use std::path::PathBuf;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let out_dir = PathBuf::from(env::var("OUT_DIR").unwrap());
    let proto_files = &[
        "proto/types.proto",
        "proto/build.proto",
        "proto/clone_ws.proto",
        "proto/data_stream.proto",
        "proto/execution.proto",
        "proto/interactive_execution.proto",
        "proto/introspection.proto",
        "proto/security.proto",
        "proto/system_utils.proto",
        "proto/file_system.proto",
        "proto/settings.proto",
        "proto/terminal.proto",
        "proto/workspace.proto",
        "proto/packages.proto",
        "proto/installer.proto",
    ];

    let proto_dirs = &["proto"];

    tonic_build::configure()
        .build_server(true)
        .build_client(true)
        .file_descriptor_set_path(out_dir.join("rqtll_descriptor.bin"))
        .compile(proto_files, proto_dirs)?;

    Ok(())
}
