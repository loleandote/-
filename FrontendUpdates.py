#!/usr/bin/python3 -u
import sys
import Ice
import IceStorm
Ice.loadSlice('urfs.ice')
import URFS
class FrontendUpdatesI(URFS.FrontendUpdates):
    def get_topic_manager(self):
        key = 'IceStorm.TopicManager.Proxy'
        proxy = self.broker.stringToProxy('IceStorm/TopicManager:tcp -p 10000')
        if proxy is None:
            print("property {} not set".format(key))
            return None

        print("Using IceStorm in: '%s'" % key)
        return IceStorm.TopicManagerPrx.checkedCast(proxy)
    def newFrontend(self, newFrontend):
        self.newFrontend = newFrontend
        self.broker = newFrontend.communicator()
        topic_mgr = self.get_topic_manager()
        if not topic_mgr:
            print('Invalid proxy')
            return 2
        print(newFrontend, flush=True)
        topic_name = "FrontendTopic"
        try:
            topic = topic_mgr.create(topic_name)
        except IceStorm.TopicExists:
            topic = topic_mgr.retrieve(topic_name)
        publisher = topic.getPublisher()
        frontend = URFS.FrontendPrx.uncheckedCast(publisher)
        frontend.replyNewFrontend(self.newFrontend)