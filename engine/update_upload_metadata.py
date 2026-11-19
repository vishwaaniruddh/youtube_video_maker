import os

projects_data = {
    '13_jadui_kaleen': {
        'title': 'जादुई कालीन की अनोखी सैर 🪄✨ | Panchatantra Moral Story | 3D Animation | Dream Byte #Shorts',
        'desc': '''कबाड़ की दुकान में पड़े पुराने कालीन पर जब आरव ने कदम रखा, तो कालीन हवा में उड़कर बादलों को चीरने लगा! जानिए क्या हुआ जब लालची सेठ ने इसे खरीदना चाहा...

👉 Subscribe to @DreamByte-y3h for daily 3D cartoon moral stories!
दोस्तों, अगर आपको यह जादुई कालीन मिले तो आप कहाँ जाएंगे? कमेंट में बताएं!

#Shorts #JaduiKaleen #MagicCarpet #HindiMoralStories #Panchatantra #3DAnimation #DreamByte #HindiKahani''',
        'tags': 'jadui kaleen,flying carpet hindi story,magic carpet,hindi moral stories,panchatantra stories in hindi,3d cartoon hindi,dreambyte,dream byte,hindi kahaniya,bedtime stories in hindi,shorts,viral shorts',
        'schedule_date': 'Nov 19, 2026',
        'schedule_time': '12:00 PM'
    },
    '14_cheenti_aur_kabootar': {
        'title': 'चींटी और कबूतर की सच्ची दोस्ती 🕊️🐜 | Panchatantra Moral Story | 3D Animation | Dream Byte #Shorts',
        'desc': '''नदी में डूबती नन्ही चींटी को कबूतर ने बचाया, और जब शिकारी ने कबूतर पर तीर ताना... तो चींटी ने सिखाया अनोखा सबक! जानिए कैसे एक छोटा दोस्त भी जान बचा सकता है!

👉 Subscribe to @DreamByte-y3h for daily 3D cartoon moral stories!
क्या आपका भी कोई ऐसा सच्चा दोस्त है? कमेंट में 'हाँ' या 'ना' बताएं!

#Shorts #CheentiAurKabootar #AntAndDove #PanchatantraStories #HindiMoralStories #DreamByte #3DAnimation #HindiKahani''',
        'tags': 'cheenti aur kabootar,ant and dove hindi story,panchatantra stories in hindi,hindi cartoon,hindi moral stories,3d cartoon hindi,dreambyte,dream byte,bachon ki kahaniya,dosti ki kahani,shorts,viral shorts',
        'schedule_date': 'Nov 19, 2026',
        'schedule_time': '05:00 PM'
    },
    '15_chamatkari_ghada': {
        'title': 'चमत्कारी घड़ा और तीन वरदान 🏺✨ | Panchatantra Moral Story | 3D Animation | Dream Byte #Shorts',
        'desc': '''खेत में मिले प्राचीन चमत्कारी घड़े में जो भी डालो, 100 गुना बनकर निकलता है! पर जब लालची ज़मींदार घड़े में खुद गिर पड़ा, तो क्या हुआ? देखिए इस मजेदार 3D एनिमेटेड कहानी में!

👉 Subscribe to @DreamByte-y3h for daily 3D cartoon moral stories!
अगर आपको ऐसा घड़ा मिले, तो आप उसमें क्या डालेंगे? कमेंट में बताएं!

#Shorts #ChamatkariGhada #MagicPot #PanchatantraStories #HindiMoralStories #DreamByte #3DAnimation #HindiStories''',
        'tags': 'chamatkari ghada,magic pot hindi kahani,panchatantra stories in hindi,hindi cartoon,moral stories in hindi,3d cartoon hindi,dreambyte,dream byte,laalchi zamindar,shorts,viral shorts',
        'schedule_date': 'Nov 20, 2026',
        'schedule_time': '12:00 PM'
    },
    '16_neela_siyaar': {
        'title': 'नीला सियार — झूठा राजा 🐺👑 | Panchatantra Moral Story | 3D Animation | Dream Byte #Shorts',
        'desc': '''नीले रंग के ड्रम में गिरकर सियार बन बैठा जंगल का राजा! शेर और चीते भी डरकर सिर झुकाने लगे... लेकिन पूर्णिमा की रात जब सियार हुआँ-हुआँ चिल्लाया, तो क्या हुआ? देखिए पूरा वीडियो!

👉 Subscribe to @DreamByte-y3h for daily 3D cartoon moral stories!
क्या आपने कभी किसी का झूठा नकाब उतरते देखा है? कमेंट में बताएं!

#Shorts #NeelaSiyaar #TheBlueJackal #PanchatantraStories #HindiMoralStories #DreamByte #3DAnimation #HindiKahani''',
        'tags': 'neela siyaar,the blue jackal hindi story,panchatantra stories in hindi,hindi cartoon,moral stories in hindi,3d cartoon hindi,dreambyte,dream byte,chatur siyaar,shorts,viral shorts',
        'schedule_date': 'Nov 20, 2026',
        'schedule_time': '05:00 PM'
    },
    '17_detective_chintu_doodh_case': {
        'title': 'जासूस चींटू और रहस्यमयी गाय का दूध 🕵️‍♂️🥛 | Detective Chintu 3D | Dream Byte #Shorts',
        'desc': '''बंद तबेले से रोज़ रात को गाय का सारा दूध रहस्यमयी तरीके से गायब हो रहा था, और ताले भी नहीं टूटे थे! जासूस चींटू ने बिछाया सफेद आटे का जाल और पकड़ा रंगे हाथों... देखिए कौन था वो चोर!

👉 Subscribe to @DreamByte-y3h for daily 3D detective mysteries!
क्या आप भी जासूस चींटू जैसे तेज़ दिमाग वाले हैं? कमेंट में बताओ!

#Shorts #DetectiveChintu #MilkHeistMystery #3DAnimation #DreamByte #HindiMystery #HindiDetectiveStories #ShortsStory''',
        'tags': 'detective chintu,jasoos chintu,mystery stories in hindi,3d cartoon hindi,dreambyte,dream byte,hindi detective cartoon,milk mystery,shorts,viral shorts',
        'schedule_date': 'Nov 21, 2026',
        'schedule_time': '12:00 PM'
    },
    '18_birbal_ki_khichdi': {
        'title': 'बीरबल की खिचड़ी 🍲🔥 | Akbar Birbal Story | 3D Animation | Dream Byte #Shorts',
        'desc': '''कड़ाके की ठंड में बर्फीले पानी में खड़े गरीब को इनाम देने से जब अकबर ने मना किया, तो बीरबल ने 10 फीट ऊपर हाँडी टांगकर पकाई अनोखी खिचड़ी! देखिए बीरबल की लाजवाब हाजिरजवाबी!

👉 Subscribe to @DreamByte-y3h for daily Akbar Birbal 3D tales!
क्या बीरबल का यह जवाब आपको सबसे अक्लमंद लगा? कमेंट में बताएं!

#Shorts #BirbalKiKhichdi #AkbarBirbal #HindiMoralStories #3DAnimation #DreamByte #HindiStories #Panchatantra''',
        'tags': 'birbal ki khichdi,akbar birbal stories,akbar birbal hindi,3d cartoon hindi,dreambyte,dream byte,hindi moral stories,chatur birbal,shorts,viral shorts',
        'schedule_date': 'Nov 21, 2026',
        'schedule_time': '05:00 PM'
    },
    '19_jadui_joota': {
        'title': 'जादुई जूता जो हवा में उड़ता था ⚡👟 | Hindi Fairy Tale | 3D Animation | Dream Byte #Shorts',
        'desc': '''गुफा में मिले चमत्कारी उड़ने वाले जूतों को पहनकर कबीर हवा में सुपरसोनिक स्पीड से उड़ने लगा! जब गाँव पर डाकुओं का हमला हुआ, तो उसने बवंडर बनकर क्या किया? देखिए इस रोमांचक 3D वीडियो में!

👉 Subscribe to @DreamByte-y3h for daily magical 3D cartoon stories!
अगर आपको ऐसे उड़ने वाले जादुई जूते मिलें, तो आप क्या करेंगे? कमेंट में बताएं!

#Shorts #JaduiJoota #FlyingShoes #HindiFairyTales #MoralStories #3DAnimation #DreamByte #HindiKahani''',
        'tags': 'jadui joota,flying shoes hindi story,magical shoes,3d cartoon hindi,dreambyte,dream byte,hindi moral stories,hindi fairy tales,action cartoon hindi,shorts,viral shorts',
        'schedule_date': 'Nov 22, 2026',
        'schedule_time': '12:00 PM'
    },
    '20_sher_aur_chuha': {
        'title': 'शेर और छोटा चूहा 🦁🐭 | Panchatantra Moral Story | 3D Animation | Dream Byte #Shorts',
        'desc': '''जंगल के खूंखार राजा शेर ने जब नन्हे चूहे को छोड़ दिया, तो चूहे ने कहा था—'मैं भी कभी काम आऊंगा!' जब शेर शिकारी के मोटे जाल में फँस गया, तो क्या चूहा शेर को बचा पाया? देखिए दिल छू लेने वाली कहानी!

👉 Subscribe to @DreamByte-y3h for daily Panchatantra 3D tales!
किसी को छोटा मत समझो! क्या आपने भी कभी किसी छोटे की बड़ी मदद देखी है? कमेंट में बताएं!

#Shorts #SherAurChuha #LionAndMouse #PanchatantraStories #HindiMoralStories #DreamByte #3DAnimation #HindiKahani''',
        'tags': 'sher aur chuha,the lion and the mouse in hindi,panchatantra stories in hindi,hindi cartoon,moral stories in hindi,3d cartoon hindi,dreambyte,dream byte,dosti ki kahani,shorts,viral shorts',
        'schedule_date': 'Nov 22, 2026',
        'schedule_time': '05:00 PM'
    }
}

for p, d in projects_data.items():
    w_dir = os.path.join(p, 'youtube_writeups')
    with open(os.path.join(w_dir, '01_TITLE_OPTIONS.txt'), 'w', encoding='utf-8') as f:
        f.write(f"OPTION 1 (Recommended):\n{d['title']}\n")
    with open(os.path.join(w_dir, '02_DESCRIPTION_AND_CHAPTERS.txt'), 'w', encoding='utf-8') as f:
        f.write(f"{d['desc']}\n")
    with open(os.path.join(w_dir, '03_TAGS_AND_HASHTAGS.txt'), 'w', encoding='utf-8') as f:
        f.write(f"{d['tags']}\n")

print("All 8 project writeups updated with custom story metadata!")
