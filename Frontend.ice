module ServerSide {
  sequence<string> sa;
  sequence<byte>bites;
  interface FileUploader{
      void upload(bites baits);
  }
  interface FileDownloader{
    bites download();
    void destroy();
  }
  interface FileManager{
    string createUploader(string file);
    FileDownloader* createDownloader(string file);
  };
  interface Frontend {
    string write(string message);
    sa list();
    //FileUploader* uploadFile(string file);
    string uploadFile(string file);
    FileDownloader* downloadFile(string file);
    void prueba(bites baits);
  };
};
