//Inbox.vue
<template>
  <div ref="talkjs" style="width: 90%; margin: 30px; height: 500px">
    <i>Loading chat...</i>
  </div>
</template> 

//Inbox.vue
<script>
  import Talk from 'talkjs';
  // import createProxyMiddleware from `http-proxy-middleware`;
  //Inbox.vue

export default {    
  
        name: 'Inbox',
        props: {
            menteeInfo: {
              type: Object,
              required: true
            },
            
            mentorInfo:{
              type: Object,
              required: true,
            }

        },
        
        data(){
          return{
           mentee_info:this.menteeInfo,
           mentor_info:this.mentorInfo,
          }
        },

        async mounted(){

          // let this = this
          
          // const proxy = createProxyMiddleware({

          //     target: 'https://app.talkjs.com',
          //     changeOrigin: true,
          //     headers: {
          //       'Access-Control-Allow-Origin': '*',
          //     },
          // });
          await Talk.ready
          console.log(this.mentee_info)
          console.log(this.mentor_info)
          const mentee = new Talk.User({
            id: String(this.menteeInfo.id),
            name: this.mentee_info.uname,
            photoUrl: this.mentee_info.profile,
            role: this.mentee_info.role
          })

          const talkSession = new Talk.Session({
            appId: 'tkGXCrqs',
            me: mentee,
          });

          const mentor = new Talk.User({
            id: String(this.mentorInfo.id),
            name: this.mentor_info.uname,
            photoUrl: this.mentor_info.profile,
            welcomeMessage: 'Hey, how can I help?',
            role: this.mentor_info.role,
          });
          

          const conversation = talkSession.getOrCreateConversation(
            Talk.oneOnOneId( mentee,mentor)
          );

          conversation.setParticipant(mentee);
          conversation.setParticipant(mentor);

          const inbox = talkSession.createInbox();
          inbox.select(conversation);

          inbox.mount(this.$refs.talkjs);
        },
        
    }
</script>