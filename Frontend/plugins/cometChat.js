import { CometChat} from "@cometchat-pro/chat";

const cometChat = new CometChat({
  appId: '232501e53e2a179b',
  region: 'eu',
  authKey: '19b358198f5b04b62388fceabf545a2ba8135930',
});

export default defineNuxtPlugin((NuxtApp => {
  CometChat.init('232501e53e2a179b');
  NuxtApp.vueApp.use(CometChat);
}))