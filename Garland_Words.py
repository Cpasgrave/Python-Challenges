"""
This is my answer to GAWEN STEASY's assignment :

Garland Words

A Garland word is one that starts and ends with the same N letters in the same order, for some N greater than 0, but less than the length of the word. N is called the garland word's degree. 

For instance, "onion" is a garland word of degree 2, because its first 2 letters "on" are the same as its last 2 letters: onion.

Write an program, that will take a word as input and output whether it's a garland word along with the corresponding degree.
"""
#############
# One Liner #
#############
print((lambda a:[i for i in range(len(a))if a[:i]==a[-i:]]or 'not')(input()))

######################
# With list of words #
######################
print('\n'.join([''.join([a,' --> ',a[:i]]) for a in (words).split() for i in range(len(a)) if a[:i] == a[-i:]]))

words = '''sense decide church meantime headache tomato underground decade photograph restore retire entertainment onion require eraser strongest murmur educated heartache ingoing antiquarian deride orator enlighten reassure delude terminate emblem enliven estates restore ethernet toronto decide church ooo template miami estimates entertainment eminem tomato educated underground alphabetical onion volvo hitachi george decade require aaa sense amsterdam photograph edited insulin
'''

print('\n'.join([''.join([a,' --> ',a[:i]]) for a in (words).split() for i in range(len(a)) if a[:i] == a[-i:]]))

mots = '''abracadabra chevauche entrelaçaient septante-sept entourent revolutionnaire entrouvrent entreprennent entre-tuaient bip-bip mecanisme entre-déchiraient entament entreprirent cricri entravent blabla entrelacent cherche désaccordés tentent entameraient entortilleraient flonflon gla-gla entravaient entretuaient entamèrent intervint entrecroisent reliure pousse-pousse entrebâillèrent entraînement entonnaient chichi entrechoquaient coin-coin bye-bye entre-dévorèrent entr'égorgent la-la-la air-air entassaient entêtement entretiendraient tonton reconnaitre gnagnagna trou-trou refractaire entretenaient doudou bulbul you-you fou-fou entrent entremêlent repertoire revendre quelque entrebâillaient entierement tête-à-tête entre-regardent entendissent zinzin guili-guili entretiennent fifty-fifty gnian-gnian entraident passe-passe rembourre tsoin-tsoin grigri vis-à-vis entreprendraient raillerai blablabla debandade devergonde rencontre entichèrent entretoisaient bibi tacatacatac bla-bla entrassent testes dondon entraînèrent agar-agar respiratoire repondre entrebâillement entendement croa-croa moi-moi-moi reactionnaire entachent zig-zig metronome anticipant entonneraient entreposent entr'appellent anticoagulant gri-gri enterrent entourèrent reproduire respiratoires bouche-à-bouche entourloupent entrelacement cinquante-cinq béribéri sentissent entamaient moitié-moitié joli-joli cracra cui-cui cache-cache temerite melodrame revoyure entement entêteraient trente-quatre entasseraient entassèrent entreprenaient entretient entichent entraîneraient errer mesdames entêtaient messieurs-dames traintrain tam-tam entérinement endocrinien redescendre entrecroisèrent frous-frous entrelacèrent entretuent enténèbrent texte gnangnan olé-olé tente refoutre roi-roi tom-tom rentrèrent rectangulaire entrebâillent entrecroisaient coupe-coupe resserres entablement reduire entrevirent fil-à-fil enterraient nestoriennes entente porte-à-porte entichement aglagla repeindre entendirent tintin entassent kifkif resoudre enterrement demande entraînent entièrement entraient underground ylang-ylang toutou tchin-tchin bouis-bouis fanfan entreregardèrent bonbon bebe bouiboui echec est-ouest mentalement ronron entoureraient antidérapant soussou cul-cul tsé-tsé entendent glouglou enthousiasmaient quelconque rentrent coucou dada entortillement entrecoupent entrouvrirent repandre relire cancan entrèrent enterrèrent meme entrechoquement gris-gris frou-frou retranscrire entremêlement zonzon pipi tenacite entortillaient entortillent youyou entretien entrainement entaillent touche-touche entretinrent demode entre-dévorent reconduire entre-tuent zzzz entre-regardèrent loulou derider entravèrent teinte boubou degringolade nounou entr'égorgèrent soussous enthousiasmèrent rendre froufrou kif-kif chouchou face-à-face boui-boui entêtent lurelure rassembleras hercher tacatac entrecoupaient refectoire rejoindre entre-déchirent recoudre chercher verve couscous crincrin islandais reprendre miam-miam tamtam dum-dum entassement teuf-teuf entremêlaient ondulation ionisation entretoisement saisissais cha-cha-cha gouzi-gouzi secousse entouraient pom-pom refaire tss-tss lesquelles chevêche entonnent entendaient entrevoyaient train-train terre-à-terre entregent secheresse aye-aye entubent glagla entrouvraient entre-déchirèrent transmettra quiqui quatre-vingt-quatre entendraient remettre antioxydant entonnèrent restreindre respires pioupiou entrechoquent jinjin bla-bla-bla reconstruire donnant-donnant tete dare-dare entreraient papa redire chou-chou descendes entretueraient neuneu entrechoquèrent gingin nanan entrecroisement deux-deux retardataire flafla entraînaient entrevoient poto-poto foufou houhou recrire joujou chienchien raseras'''
