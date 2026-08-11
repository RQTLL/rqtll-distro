pub mod rqtll {
    pub mod api {
        pub mod v1 {
            tonic::include_proto!("rqtll.api.v1");
            pub const FILE_DESCRIPTOR_SET: &[u8] = tonic::include_file_descriptor_set!("rqtll_descriptor");
        }
    }
}
