module URFS {
  struct FileInfo {
    string name;
    string hash;
  };
  exception FileNameInUseError {};
  exception FileNotFoundError {};
  exception FileAlreadyExistsError {
    string hash;
  };
  sequence<FileInfo> FileList;
 interface Uploader {
    void send(string data);
    FileInfo save()
      throws FileAlreadyExistsError;
    void destroy();
  };
  interface Downloader {
    string recv(int size);
    void destroy();
  };
  interface FileManager {
    Uploader* createUploader(string filename);
    Downloader* createDownloader(string hash)
      throws FileNotFoundError;
    void removeFile(string hash)
      throws FileNotFoundError;
  };
  interface Frontend {
    FileList getFileList();
    Uploader* uploadFile(string filename)
      throws FileNameInUseError;
    Downloader* downloadFile(string hash)
      throws FileNotFoundError;
    FileInfo getFileInfo(string hash)
      throws FileNotFoundError;
    void removeFile(string hash)
      throws FileNotFoundError;

    void replyNewFrontend(Frontend* oldFrontend);
  };
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
