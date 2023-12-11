module ServerSide {
  sequence<string> sa;
  sequence<byte>bites;
  interface FileUploader{
      void upload(bites baits);
  }
  interface FileDownloader{
    bites download();
  }
  interface Frontend {
    string write(string message);
    sa list();
    FileUploader* uploadFile(string file);
    FileDownloader* downloadFile(string file);
    void prueba(bites baits);
  };
  interface FileManager{
    FileUploader* createUploader(string file);
    FileDownloader* createDownloader(string file);
  };
};
