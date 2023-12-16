# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.9
#
# <auto-generated>
#
# Generated from file `Frontend.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module ServerSide
_M_ServerSide = Ice.openModule('ServerSide')
__name__ = 'ServerSide'

if '_t_sa' not in _M_ServerSide.__dict__:
    _M_ServerSide._t_sa = IcePy.defineSequence('::ServerSide::sa', (), IcePy._t_string)

if '_t_bites' not in _M_ServerSide.__dict__:
    _M_ServerSide._t_bites = IcePy.defineSequence('::ServerSide::bites', (), IcePy._t_byte)

_M_ServerSide._t_FileUploader = IcePy.defineValue('::ServerSide::FileUploader', Ice.Value, -1, (), False, True, None, ())

if 'FileUploaderPrx' not in _M_ServerSide.__dict__:
    _M_ServerSide.FileUploaderPrx = Ice.createTempClass()
    class FileUploaderPrx(Ice.ObjectPrx):

        def upload(self, baits, context=None):
            return _M_ServerSide.FileUploader._op_upload.invoke(self, ((baits, ), context))

        def uploadAsync(self, baits, context=None):
            return _M_ServerSide.FileUploader._op_upload.invokeAsync(self, ((baits, ), context))

        def begin_upload(self, baits, _response=None, _ex=None, _sent=None, context=None):
            return _M_ServerSide.FileUploader._op_upload.begin(self, ((baits, ), _response, _ex, _sent, context))

        def end_upload(self, _r):
            return _M_ServerSide.FileUploader._op_upload.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_ServerSide.FileUploaderPrx.ice_checkedCast(proxy, '::ServerSide::FileUploader', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_ServerSide.FileUploaderPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::ServerSide::FileUploader'
    _M_ServerSide._t_FileUploaderPrx = IcePy.defineProxy('::ServerSide::FileUploader', FileUploaderPrx)

    _M_ServerSide.FileUploaderPrx = FileUploaderPrx
    del FileUploaderPrx

    _M_ServerSide.FileUploader = Ice.createTempClass()
    class FileUploader(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::ServerSide::FileUploader')

        def ice_id(self, current=None):
            return '::ServerSide::FileUploader'

        @staticmethod
        def ice_staticId():
            return '::ServerSide::FileUploader'

        def upload(self, baits, current=None):
            raise NotImplementedError("servant method 'upload' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_ServerSide._t_FileUploaderDisp)

        __repr__ = __str__

    _M_ServerSide._t_FileUploaderDisp = IcePy.defineClass('::ServerSide::FileUploader', FileUploader, (), None, ())
    FileUploader._ice_type = _M_ServerSide._t_FileUploaderDisp

    FileUploader._op_upload = IcePy.Operation('upload', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_ServerSide._t_bites, False, 0),), (), None, ())

    _M_ServerSide.FileUploader = FileUploader
    del FileUploader

_M_ServerSide._t_FileDownloader = IcePy.defineValue('::ServerSide::FileDownloader', Ice.Value, -1, (), False, True, None, ())

if 'FileDownloaderPrx' not in _M_ServerSide.__dict__:
    _M_ServerSide.FileDownloaderPrx = Ice.createTempClass()
    class FileDownloaderPrx(Ice.ObjectPrx):

        def download(self, context=None):
            return _M_ServerSide.FileDownloader._op_download.invoke(self, ((), context))

        def downloadAsync(self, context=None):
            return _M_ServerSide.FileDownloader._op_download.invokeAsync(self, ((), context))

        def begin_download(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_ServerSide.FileDownloader._op_download.begin(self, ((), _response, _ex, _sent, context))

        def end_download(self, _r):
            return _M_ServerSide.FileDownloader._op_download.end(self, _r)

        def destoy(self, context=None):
            return _M_ServerSide.FileDownloader._op_destoy.invoke(self, ((), context))

        def destoyAsync(self, context=None):
            return _M_ServerSide.FileDownloader._op_destoy.invokeAsync(self, ((), context))

        def begin_destoy(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_ServerSide.FileDownloader._op_destoy.begin(self, ((), _response, _ex, _sent, context))

        def end_destoy(self, _r):
            return _M_ServerSide.FileDownloader._op_destoy.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_ServerSide.FileDownloaderPrx.ice_checkedCast(proxy, '::ServerSide::FileDownloader', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_ServerSide.FileDownloaderPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::ServerSide::FileDownloader'
    _M_ServerSide._t_FileDownloaderPrx = IcePy.defineProxy('::ServerSide::FileDownloader', FileDownloaderPrx)

    _M_ServerSide.FileDownloaderPrx = FileDownloaderPrx
    del FileDownloaderPrx

    _M_ServerSide.FileDownloader = Ice.createTempClass()
    class FileDownloader(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::ServerSide::FileDownloader')

        def ice_id(self, current=None):
            return '::ServerSide::FileDownloader'

        @staticmethod
        def ice_staticId():
            return '::ServerSide::FileDownloader'

        def download(self, current=None):
            raise NotImplementedError("servant method 'download' not implemented")

        def destoy(self, current=None):
            raise NotImplementedError("servant method 'destoy' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_ServerSide._t_FileDownloaderDisp)

        __repr__ = __str__

    _M_ServerSide._t_FileDownloaderDisp = IcePy.defineClass('::ServerSide::FileDownloader', FileDownloader, (), None, ())
    FileDownloader._ice_type = _M_ServerSide._t_FileDownloaderDisp

    FileDownloader._op_download = IcePy.Operation('download', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_ServerSide._t_bites, False, 0), ())
    FileDownloader._op_destoy = IcePy.Operation('destoy', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())

    _M_ServerSide.FileDownloader = FileDownloader
    del FileDownloader

_M_ServerSide._t_FileManager = IcePy.defineValue('::ServerSide::FileManager', Ice.Value, -1, (), False, True, None, ())

if 'FileManagerPrx' not in _M_ServerSide.__dict__:
    _M_ServerSide.FileManagerPrx = Ice.createTempClass()
    class FileManagerPrx(Ice.ObjectPrx):

        def createUploader(self, file, context=None):
            return _M_ServerSide.FileManager._op_createUploader.invoke(self, ((file, ), context))

        def createUploaderAsync(self, file, context=None):
            return _M_ServerSide.FileManager._op_createUploader.invokeAsync(self, ((file, ), context))

        def begin_createUploader(self, file, _response=None, _ex=None, _sent=None, context=None):
            return _M_ServerSide.FileManager._op_createUploader.begin(self, ((file, ), _response, _ex, _sent, context))

        def end_createUploader(self, _r):
            return _M_ServerSide.FileManager._op_createUploader.end(self, _r)

        def createDownloader(self, file, context=None):
            return _M_ServerSide.FileManager._op_createDownloader.invoke(self, ((file, ), context))

        def createDownloaderAsync(self, file, context=None):
            return _M_ServerSide.FileManager._op_createDownloader.invokeAsync(self, ((file, ), context))

        def begin_createDownloader(self, file, _response=None, _ex=None, _sent=None, context=None):
            return _M_ServerSide.FileManager._op_createDownloader.begin(self, ((file, ), _response, _ex, _sent, context))

        def end_createDownloader(self, _r):
            return _M_ServerSide.FileManager._op_createDownloader.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_ServerSide.FileManagerPrx.ice_checkedCast(proxy, '::ServerSide::FileManager', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_ServerSide.FileManagerPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::ServerSide::FileManager'
    _M_ServerSide._t_FileManagerPrx = IcePy.defineProxy('::ServerSide::FileManager', FileManagerPrx)

    _M_ServerSide.FileManagerPrx = FileManagerPrx
    del FileManagerPrx

    _M_ServerSide.FileManager = Ice.createTempClass()
    class FileManager(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::ServerSide::FileManager')

        def ice_id(self, current=None):
            return '::ServerSide::FileManager'

        @staticmethod
        def ice_staticId():
            return '::ServerSide::FileManager'

        def createUploader(self, file, current=None):
            raise NotImplementedError("servant method 'createUploader' not implemented")

        def createDownloader(self, file, current=None):
            raise NotImplementedError("servant method 'createDownloader' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_ServerSide._t_FileManagerDisp)

        __repr__ = __str__

    _M_ServerSide._t_FileManagerDisp = IcePy.defineClass('::ServerSide::FileManager', FileManager, (), None, ())
    FileManager._ice_type = _M_ServerSide._t_FileManagerDisp

    FileManager._op_createUploader = IcePy.Operation('createUploader', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), IcePy._t_string, False, 0), ())
    FileManager._op_createDownloader = IcePy.Operation('createDownloader', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_ServerSide._t_FileDownloaderPrx, False, 0), ())

    _M_ServerSide.FileManager = FileManager
    del FileManager

_M_ServerSide._t_Frontend = IcePy.defineValue('::ServerSide::Frontend', Ice.Value, -1, (), False, True, None, ())

if 'FrontendPrx' not in _M_ServerSide.__dict__:
    _M_ServerSide.FrontendPrx = Ice.createTempClass()
    class FrontendPrx(Ice.ObjectPrx):

        def write(self, message, context=None):
            return _M_ServerSide.Frontend._op_write.invoke(self, ((message, ), context))

        def writeAsync(self, message, context=None):
            return _M_ServerSide.Frontend._op_write.invokeAsync(self, ((message, ), context))

        def begin_write(self, message, _response=None, _ex=None, _sent=None, context=None):
            return _M_ServerSide.Frontend._op_write.begin(self, ((message, ), _response, _ex, _sent, context))

        def end_write(self, _r):
            return _M_ServerSide.Frontend._op_write.end(self, _r)

        def list(self, context=None):
            return _M_ServerSide.Frontend._op_list.invoke(self, ((), context))

        def listAsync(self, context=None):
            return _M_ServerSide.Frontend._op_list.invokeAsync(self, ((), context))

        def begin_list(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_ServerSide.Frontend._op_list.begin(self, ((), _response, _ex, _sent, context))

        def end_list(self, _r):
            return _M_ServerSide.Frontend._op_list.end(self, _r)

        def uploadFile(self, file, context=None):
            return _M_ServerSide.Frontend._op_uploadFile.invoke(self, ((file, ), context))

        def uploadFileAsync(self, file, context=None):
            return _M_ServerSide.Frontend._op_uploadFile.invokeAsync(self, ((file, ), context))

        def begin_uploadFile(self, file, _response=None, _ex=None, _sent=None, context=None):
            return _M_ServerSide.Frontend._op_uploadFile.begin(self, ((file, ), _response, _ex, _sent, context))

        def end_uploadFile(self, _r):
            return _M_ServerSide.Frontend._op_uploadFile.end(self, _r)

        def downloadFile(self, file, context=None):
            return _M_ServerSide.Frontend._op_downloadFile.invoke(self, ((file, ), context))

        def downloadFileAsync(self, file, context=None):
            return _M_ServerSide.Frontend._op_downloadFile.invokeAsync(self, ((file, ), context))

        def begin_downloadFile(self, file, _response=None, _ex=None, _sent=None, context=None):
            return _M_ServerSide.Frontend._op_downloadFile.begin(self, ((file, ), _response, _ex, _sent, context))

        def end_downloadFile(self, _r):
            return _M_ServerSide.Frontend._op_downloadFile.end(self, _r)

        def prueba(self, baits, context=None):
            return _M_ServerSide.Frontend._op_prueba.invoke(self, ((baits, ), context))

        def pruebaAsync(self, baits, context=None):
            return _M_ServerSide.Frontend._op_prueba.invokeAsync(self, ((baits, ), context))

        def begin_prueba(self, baits, _response=None, _ex=None, _sent=None, context=None):
            return _M_ServerSide.Frontend._op_prueba.begin(self, ((baits, ), _response, _ex, _sent, context))

        def end_prueba(self, _r):
            return _M_ServerSide.Frontend._op_prueba.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_ServerSide.FrontendPrx.ice_checkedCast(proxy, '::ServerSide::Frontend', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_ServerSide.FrontendPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::ServerSide::Frontend'
    _M_ServerSide._t_FrontendPrx = IcePy.defineProxy('::ServerSide::Frontend', FrontendPrx)

    _M_ServerSide.FrontendPrx = FrontendPrx
    del FrontendPrx

    _M_ServerSide.Frontend = Ice.createTempClass()
    class Frontend(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::ServerSide::Frontend')

        def ice_id(self, current=None):
            return '::ServerSide::Frontend'

        @staticmethod
        def ice_staticId():
            return '::ServerSide::Frontend'

        def write(self, message, current=None):
            raise NotImplementedError("servant method 'write' not implemented")

        def list(self, current=None):
            raise NotImplementedError("servant method 'list' not implemented")

        def uploadFile(self, file, current=None):
            raise NotImplementedError("servant method 'uploadFile' not implemented")

        def downloadFile(self, file, current=None):
            raise NotImplementedError("servant method 'downloadFile' not implemented")

        def prueba(self, baits, current=None):
            raise NotImplementedError("servant method 'prueba' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_ServerSide._t_FrontendDisp)

        __repr__ = __str__

    _M_ServerSide._t_FrontendDisp = IcePy.defineClass('::ServerSide::Frontend', Frontend, (), None, ())
    Frontend._ice_type = _M_ServerSide._t_FrontendDisp

    Frontend._op_write = IcePy.Operation('write', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), IcePy._t_string, False, 0), ())
    Frontend._op_list = IcePy.Operation('list', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_ServerSide._t_sa, False, 0), ())
    Frontend._op_uploadFile = IcePy.Operation('uploadFile', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), IcePy._t_string, False, 0), ())
    Frontend._op_downloadFile = IcePy.Operation('downloadFile', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_ServerSide._t_FileDownloaderPrx, False, 0), ())
    Frontend._op_prueba = IcePy.Operation('prueba', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_ServerSide._t_bites, False, 0),), (), None, ())

    _M_ServerSide.Frontend = Frontend
    del Frontend

# End of module ServerSide