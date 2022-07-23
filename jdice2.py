#######################################################
# jdice2 revised July 2022
#######################################################

# Original Method: https://armantheparman.com/bitcoin-seed-with-dice/
# Verify: https://iancoleman.io/bip39/


import random
import hashlib

wordbank = {'h1111': 'abandon', 'h1112': 'ability', 'h1113': 'able', 'h1114': 'about', 'h1115': 'above',
            'h1116': 'absent', 'h1121': 'absorb', 'h1122': 'abstract', 'h1123': 'absurd', 'h1124': 'abuse',
            'h1125': 'access', 'h1126': 'accident', 'h1131': 'account', 'h1132': 'accuse', 'h1133': 'achieve',
            'h1134': 'acid', 'h1135': 'acoustic', 'h1136': 'acquire', 'h1141': 'across', 'h1142': 'act',
            'h1143': 'action', 'h1144': 'actor', 'h1145': 'actress', 'h1146': 'actual', 'h1151': 'adapt',
            'h1152': 'add', 'h1153': 'addict', 'h1154': 'address', 'h1155': 'adjust', 'h1156': 'admit',
            'h1161': 'adult', 'h1162': 'advance', 'h1163': 'advice', 'h1164': 'aerobic', 'h1165': 'affair',
            'h1166': 'afford', 'h1211': 'afraid', 'h1212': 'again', 'h1213': 'age', 'h1214': 'agent', 'h1215': 'agree',
            'h1216': 'ahead', 'h1221': 'aim', 'h1222': 'air', 'h1223': 'airport', 'h1224': 'aisle', 'h1225': 'alarm',
            'h1226': 'album', 'h1231': 'alcohol', 'h1232': 'alert', 'h1233': 'alien', 'h1234': 'all', 'h1235': 'alley',
            'h1236': 'allow', 'h1241': 'almost', 'h1242': 'alone', 'h1243': 'alpha', 'h1244': 'already',
            'h1245': 'also', 'h1246': 'alter', 'h1251': 'always', 'h1252': 'amateur', 'h1253': 'amazing',
            'h1254': 'among', 'h1255': 'amount', 'h1256': 'amused', 'h1261': 'analyst', 'h1262': 'anchor',
            'h1263': 'ancient', 'h1264': 'anger', 'h1265': 'angle', 'h1266': 'angry', 'h1311': 'animal',
            'h1312': 'ankle', 'h1313': 'announce', 'h1314': 'annual', 'h1315': 'another', 'h1316': 'answer',
            'h1321': 'antenna', 'h1322': 'antique', 'h1323': 'anxiety', 'h1324': 'any', 'h1325': 'apart',
            'h1326': 'apology', 'h1331': 'appear', 'h1332': 'apple', 'h1333': 'approve', 'h1334': 'april',
            'h1335': 'arch', 'h1336': 'arctic', 'h1341': 'area', 'h1342': 'arena', 'h1343': 'argue', 'h1344': 'arm',
            'h1345': 'armed', 'h1346': 'armor', 'h1351': 'army', 'h1352': 'around', 'h1353': 'arrange',
            'h1354': 'arrest', 'h1355': 'arrive', 'h1356': 'arrow', 'h1361': 'art', 'h1362': 'artefact',
            'h1363': 'artist', 'h1364': 'artwork', 'h1365': 'ask', 'h1366': 'aspect', 'h1411': 'assault',
            'h1412': 'asset', 'h1413': 'assist', 'h1414': 'assume', 'h1415': 'asthma', 'h1416': 'athlete',
            'h1421': 'atom', 'h1422': 'attack', 'h1423': 'attend', 'h1424': 'attitude', 'h1425': 'attract',
            'h1426': 'auction', 'h1431': 'audit', 'h1432': 'august', 'h1433': 'aunt', 'h1434': 'author',
            'h1435': 'auto', 'h1436': 'autumn', 'h1441': 'average', 'h1442': 'avocado', 'h1443': 'avoid',
            'h1444': 'awake', 'h1445': 'aware', 'h1446': 'away', 'h1451': 'awesome', 'h1452': 'awful',
            'h1453': 'awkward', 'h1454': 'axis', 'h1455': 'baby', 'h1456': 'bachelor', 'h1461': 'bacon',
            'h1462': 'badge', 'h1463': 'bag', 'h1464': 'balance', 'h1465': 'balcony', 'h1466': 'ball',
            'h1511': 'bamboo', 'h1512': 'banana', 'h1513': 'banner', 'h1514': 'bar', 'h1515': 'barely',
            'h1516': 'bargain', 'h1521': 'barrel', 'h1522': 'base', 'h1523': 'basic', 'h1524': 'basket',
            'h1525': 'battle', 'h1526': 'beach', 'h1531': 'bean', 'h1532': 'beauty', 'h1533': 'because',
            'h1534': 'become', 'h1535': 'beef', 'h1536': 'before', 'h1541': 'begin', 'h1542': 'behave',
            'h1543': 'behind', 'h1544': 'believe', 'h1545': 'below', 'h1546': 'belt', 'h1551': 'bench',
            'h1552': 'benefit', 'h1553': 'best', 'h1554': 'betray', 'h1555': 'better', 'h1556': 'between',
            'h1561': 'beyond', 'h1562': 'bicycle', 'h1563': 'bid', 'h1564': 'bike', 'h1565': 'bind', 'h1566': 'biology',
            'h1611': 'bird', 'h1612': 'birth', 'h1613': 'bitter', 'h1614': 'black', 'h1615': 'blade', 'h1616': 'blame',
            'h1621': 'blanket', 'h1622': 'blast', 'h1623': 'bleak', 'h1624': 'bless', 'h1625': 'blind',
            'h1626': 'blood', 'h1631': 'blossom', 'h1632': 'blouse', 'h1633': 'blue', 'h1634': 'blur', 'h1635': 'blush',
            'h1636': 'board', 'h1641': 'boat', 'h1642': 'body', 'h1643': 'boil', 'h1644': 'bomb', 'h1645': 'bone',
            'h1646': 'bonus', 'h1651': 'book', 'h1652': 'boost', 'h1653': 'border', 'h1654': 'boring',
            'h1655': 'borrow', 'h1656': 'boss', 'h1661': 'bottom', 'h1662': 'bounce', 'h1663': 'box', 'h1664': 'boy',
            'h1665': 'bracket', 'h1666': 'brain', 'h2111': 'brand', 'h2112': 'brass', 'h2113': 'brave',
            'h2114': 'bread', 'h2115': 'breeze', 'h2116': 'brick', 'h2121': 'bridge', 'h2122': 'brief',
            'h2123': 'bright', 'h2124': 'bring', 'h2125': 'brisk', 'h2126': 'broccoli', 'h2131': 'broken',
            'h2132': 'bronze', 'h2133': 'broom', 'h2134': 'brother', 'h2135': 'brown', 'h2136': 'brush',
            'h2141': 'bubble', 'h2142': 'buddy', 'h2143': 'budget', 'h2144': 'buffalo', 'h2145': 'build',
            'h2146': 'bulb', 'h2151': 'bulk', 'h2152': 'bullet', 'h2153': 'bundle', 'h2154': 'bunker',
            'h2155': 'burden', 'h2156': 'burger', 'h2161': 'burst', 'h2162': 'bus', 'h2163': 'business',
            'h2164': 'busy', 'h2165': 'butter', 'h2166': 'buyer', 'h2211': 'buzz', 'h2212': 'cabbage', 'h2213': 'cabin',
            'h2214': 'cable', 'h2215': 'cactus', 'h2216': 'cage', 'h2221': 'cake', 'h2222': 'call', 'h2223': 'calm',
            'h2224': 'camera', 'h2225': 'camp', 'h2226': 'can', 'h2231': 'canal', 'h2232': 'cancel', 'h2233': 'candy',
            'h2234': 'cannon', 'h2235': 'canoe', 'h2236': 'canvas', 'h2241': 'canyon', 'h2242': 'capable',
            'h2243': 'capital', 'h2244': 'captain', 'h2245': 'car', 'h2246': 'carbon', 'h2251': 'card',
            'h2252': 'cargo', 'h2253': 'carpet', 'h2254': 'carry', 'h2255': 'cart', 'h2256': 'case', 'h2261': 'cash',
            'h2262': 'casino', 'h2263': 'castle', 'h2264': 'casual', 'h2265': 'cat', 'h2266': 'catalog',
            'h2311': 'catch', 'h2312': 'category', 'h2313': 'cattle', 'h2314': 'caught', 'h2315': 'cause',
            'h2316': 'caution', 'h2321': 'cave', 'h2322': 'ceiling', 'h2323': 'celery', 'h2324': 'cement',
            'h2325': 'census', 'h2326': 'century', 'h2331': 'cereal', 'h2332': 'certain', 'h2333': 'chair',
            'h2334': 'chalk', 'h2335': 'champion', 'h2336': 'change', 'h2341': 'chaos', 'h2342': 'chapter',
            'h2343': 'charge', 'h2344': 'chase', 'h2345': 'chat', 'h2346': 'cheap', 'h2351': 'check', 'h2352': 'cheese',
            'h2353': 'chef', 'h2354': 'cherry', 'h2355': 'chest', 'h2356': 'chicken', 'h2361': 'chief',
            'h2362': 'child', 'h2363': 'chimney', 'h2364': 'choice', 'h2365': 'choose', 'h2366': 'chronic',
            'h2411': 'chuckle', 'h2412': 'chunk', 'h2413': 'churn', 'h2414': 'cigar', 'h2415': 'cinnamon',
            'h2416': 'circle', 'h2421': 'citizen', 'h2422': 'city', 'h2423': 'civil', 'h2424': 'claim', 'h2425': 'clap',
            'h2426': 'clarify', 'h2431': 'claw', 'h2432': 'clay', 'h2433': 'clean', 'h2434': 'clerk', 'h2435': 'clever',
            'h2436': 'click', 'h2441': 'client', 'h2442': 'cliff', 'h2443': 'climb', 'h2444': 'clinic', 'h2445': 'clip',
            'h2446': 'clock', 'h2451': 'clog', 'h2452': 'close', 'h2453': 'cloth', 'h2454': 'cloud', 'h2455': 'clown',
            'h2456': 'club', 'h2461': 'clump', 'h2462': 'cluster', 'h2463': 'clutch', 'h2464': 'coach',
            'h2465': 'coast', 'h2466': 'coconut', 'h2511': 'code', 'h2512': 'coffee', 'h2513': 'coil', 'h2514': 'coin',
            'h2515': 'collect', 'h2516': 'color', 'h2521': 'column', 'h2522': 'combine', 'h2523': 'come',
            'h2524': 'comfort', 'h2525': 'comic', 'h2526': 'common', 'h2531': 'company', 'h2532': 'concert',
            'h2533': 'conduct', 'h2534': 'confirm', 'h2535': 'congress', 'h2536': 'connect', 'h2541': 'consider',
            'h2542': 'control', 'h2543': 'convince', 'h2544': 'cook', 'h2545': 'cool', 'h2546': 'copper',
            'h2551': 'copy', 'h2552': 'coral', 'h2553': 'core', 'h2554': 'corn', 'h2555': 'correct', 'h2556': 'cost',
            'h2561': 'cotton', 'h2562': 'couch', 'h2563': 'country', 'h2564': 'couple', 'h2565': 'course',
            'h2566': 'cousin', 'h2611': 'cover', 'h2612': 'coyote', 'h2613': 'crack', 'h2614': 'cradle',
            'h2615': 'craft', 'h2616': 'cram', 'h2621': 'crane', 'h2622': 'crash', 'h2623': 'crater', 'h2624': 'crawl',
            'h2625': 'crazy', 'h2626': 'cream', 'h2631': 'credit', 'h2632': 'creek', 'h2633': 'crew',
            'h2634': 'cricket', 'h2635': 'crime', 'h2636': 'crisp', 'h2641': 'critic', 'h2642': 'crop',
            'h2643': 'cross', 'h2644': 'crouch', 'h2645': 'crowd', 'h2646': 'crucial', 'h2651': 'cruel',
            'h2652': 'cruise', 'h2653': 'crumble', 'h2654': 'crunch', 'h2655': 'crush', 'h2656': 'cry',
            'h2661': 'crystal', 'h2662': 'cube', 'h2663': 'culture', 'h2664': 'cup', 'h2665': 'cupboard',
            'h2666': 'curious', 'h3111': 'current', 'h3112': 'curtain', 'h3113': 'curve', 'h3114': 'cushion',
            'h3115': 'custom', 'h3116': 'cute', 'h3121': 'cycle', 'h3122': 'dad', 'h3123': 'damage', 'h3124': 'damp',
            'h3125': 'dance', 'h3126': 'danger', 'h3131': 'daring', 'h3132': 'dash', 'h3133': 'daughter',
            'h3134': 'dawn', 'h3135': 'day', 'h3136': 'deal', 'h3141': 'debate', 'h3142': 'debris', 'h3143': 'decade',
            'h3144': 'december', 'h3145': 'decide', 'h3146': 'decline', 'h3151': 'decorate', 'h3152': 'decrease',
            'h3153': 'deer', 'h3154': 'defense', 'h3155': 'define', 'h3156': 'defy', 'h3161': 'degree',
            'h3162': 'delay', 'h3163': 'deliver', 'h3164': 'demand', 'h3165': 'demise', 'h3166': 'denial',
            'h3211': 'dentist', 'h3212': 'deny', 'h3213': 'depart', 'h3214': 'depend', 'h3215': 'deposit',
            'h3216': 'depth', 'h3221': 'deputy', 'h3222': 'derive', 'h3223': 'describe', 'h3224': 'desert',
            'h3225': 'design', 'h3226': 'desk', 'h3231': 'despair', 'h3232': 'destroy', 'h3233': 'detail',
            'h3234': 'detect', 'h3235': 'develop', 'h3236': 'device', 'h3241': 'devote', 'h3242': 'diagram',
            'h3243': 'dial', 'h3244': 'diamond', 'h3245': 'diary', 'h3246': 'dice', 'h3251': 'diesel', 'h3252': 'diet',
            'h3253': 'differ', 'h3254': 'digital', 'h3255': 'dignity', 'h3256': 'dilemma', 'h3261': 'dinner',
            'h3262': 'dinosaur', 'h3263': 'direct', 'h3264': 'dirt', 'h3265': 'disagree', 'h3266': 'discover',
            'h3311': 'disease', 'h3312': 'dish', 'h3313': 'dismiss', 'h3314': 'disorder', 'h3315': 'display',
            'h3316': 'distance', 'h3321': 'divert', 'h3322': 'divide', 'h3323': 'divorce', 'h3324': 'dizzy',
            'h3325': 'doctor', 'h3326': 'document', 'h3331': 'dog', 'h3332': 'doll', 'h3333': 'dolphin',
            'h3334': 'domain', 'h3335': 'donate', 'h3336': 'donkey', 'h3341': 'donor', 'h3342': 'door', 'h3343': 'dose',
            'h3344': 'double', 'h3345': 'dove', 'h3346': 'draft', 'h3351': 'dragon', 'h3352': 'drama',
            'h3353': 'drastic', 'h3354': 'draw', 'h3355': 'dream', 'h3356': 'dress', 'h3361': 'drift', 'h3362': 'drill',
            'h3363': 'drink', 'h3364': 'drip', 'h3365': 'drive', 'h3366': 'drop', 'h3411': 'drum', 'h3412': 'dry',
            'h3413': 'duck', 'h3414': 'dumb', 'h3415': 'dune', 'h3416': 'during', 'h3421': 'dust', 'h3422': 'dutch',
            'h3423': 'duty', 'h3424': 'dwarf', 'h3425': 'dynamic', 'h3426': 'eager', 'h3431': 'eagle', 'h3432': 'early',
            'h3433': 'earn', 'h3434': 'earth', 'h3435': 'easily', 'h3436': 'east', 'h3441': 'easy', 'h3442': 'echo',
            'h3443': 'ecology', 'h3444': 'economy', 'h3445': 'edge', 'h3446': 'edit', 'h3451': 'educate',
            'h3452': 'effort', 'h3453': 'egg', 'h3454': 'eight', 'h3455': 'either', 'h3456': 'elbow', 'h3461': 'elder',
            'h3462': 'electric', 'h3463': 'elegant', 'h3464': 'element', 'h3465': 'elephant', 'h3466': 'elevator',
            'h3511': 'elite', 'h3512': 'else', 'h3513': 'embark', 'h3514': 'embody', 'h3515': 'embrace',
            'h3516': 'emerge', 'h3521': 'emotion', 'h3522': 'employ', 'h3523': 'empower', 'h3524': 'empty',
            'h3525': 'enable', 'h3526': 'enact', 'h3531': 'end', 'h3532': 'endless', 'h3533': 'endorse',
            'h3534': 'enemy', 'h3535': 'energy', 'h3536': 'enforce', 'h3541': 'engage', 'h3542': 'engine',
            'h3543': 'enhance', 'h3544': 'enjoy', 'h3545': 'enlist', 'h3546': 'enough', 'h3551': 'enrich',
            'h3552': 'enroll', 'h3553': 'ensure', 'h3554': 'enter', 'h3555': 'entire', 'h3556': 'entry',
            'h3561': 'envelope', 'h3562': 'episode', 'h3563': 'equal', 'h3564': 'equip', 'h3565': 'era',
            'h3566': 'erase', 'h3611': 'erode', 'h3612': 'erosion', 'h3613': 'error', 'h3614': 'erupt',
            'h3615': 'escape', 'h3616': 'essay', 'h3621': 'essence', 'h3622': 'estate', 'h3623': 'eternal',
            'h3624': 'ethics', 'h3625': 'evidence', 'h3626': 'evil', 'h3631': 'evoke', 'h3632': 'evolve',
            'h3633': 'exact', 'h3634': 'example', 'h3635': 'excess', 'h3636': 'exchange', 'h3641': 'excite',
            'h3642': 'exclude', 'h3643': 'excuse', 'h3644': 'execute', 'h3645': 'exercise', 'h3646': 'exhaust',
            'h3651': 'exhibit', 'h3652': 'exile', 'h3653': 'exist', 'h3654': 'exit', 'h3655': 'exotic',
            'h3656': 'expand', 'h3661': 'expect', 'h3662': 'expire', 'h3663': 'explain', 'h3664': 'expose',
            'h3665': 'express', 'h3666': 'extend', 'h4111': 'extra', 'h4112': 'eye', 'h4113': 'eyebrow',
            'h4114': 'fabric', 'h4115': 'face', 'h4116': 'faculty', 'h4121': 'fade', 'h4122': 'faint', 'h4123': 'faith',
            'h4124': 'fall', 'h4125': 'FALSE', 'h4126': 'fame', 'h4131': 'family', 'h4132': 'famous', 'h4133': 'fan',
            'h4134': 'fancy', 'h4135': 'fantasy', 'h4136': 'farm', 'h4141': 'fashion', 'h4142': 'fat', 'h4143': 'fatal',
            'h4144': 'father', 'h4145': 'fatigue', 'h4146': 'fault', 'h4151': 'favorite', 'h4152': 'feature',
            'h4153': 'february', 'h4154': 'federal', 'h4155': 'fee', 'h4156': 'feed', 'h4161': 'feel',
            'h4162': 'female', 'h4163': 'fence', 'h4164': 'festival', 'h4165': 'fetch', 'h4166': 'fever',
            'h4211': 'few', 'h4212': 'fiber', 'h4213': 'fiction', 'h4214': 'field', 'h4215': 'figure', 'h4216': 'file',
            'h4221': 'film', 'h4222': 'filter', 'h4223': 'final', 'h4224': 'find', 'h4225': 'fine', 'h4226': 'finger',
            'h4231': 'finish', 'h4232': 'fire', 'h4233': 'firm', 'h4234': 'first', 'h4235': 'fiscal', 'h4236': 'fish',
            'h4241': 'fit', 'h4242': 'fitness', 'h4243': 'fix', 'h4244': 'flag', 'h4245': 'flame', 'h4246': 'flash',
            'h4251': 'flat', 'h4252': 'flavor', 'h4253': 'flee', 'h4254': 'flight', 'h4255': 'flip', 'h4256': 'float',
            'h4261': 'flock', 'h4262': 'floor', 'h4263': 'flower', 'h4264': 'fluid', 'h4265': 'flush', 'h4266': 'fly',
            'h4311': 'foam', 'h4312': 'focus', 'h4313': 'fog', 'h4314': 'foil', 'h4315': 'fold', 'h4316': 'follow',
            'h4321': 'food', 'h4322': 'foot', 'h4323': 'force', 'h4324': 'forest', 'h4325': 'forget', 'h4326': 'fork',
            'h4331': 'fortune', 'h4332': 'forum', 'h4333': 'forward', 'h4334': 'fossil', 'h4335': 'foster',
            'h4336': 'found', 'h4341': 'fox', 'h4342': 'fragile', 'h4343': 'frame', 'h4344': 'frequent',
            'h4345': 'fresh', 'h4346': 'friend', 'h4351': 'fringe', 'h4352': 'frog', 'h4353': 'front', 'h4354': 'frost',
            'h4355': 'frown', 'h4356': 'frozen', 'h4361': 'fruit', 'h4362': 'fuel', 'h4363': 'fun', 'h4364': 'funny',
            'h4365': 'furnace', 'h4366': 'fury', 'h4411': 'future', 'h4412': 'gadget', 'h4413': 'gain',
            'h4414': 'galaxy', 'h4415': 'gallery', 'h4416': 'game', 'h4421': 'gap', 'h4422': 'garage',
            'h4423': 'garbage', 'h4424': 'garden', 'h4425': 'garlic', 'h4426': 'garment', 'h4431': 'gas',
            'h4432': 'gasp', 'h4433': 'gate', 'h4434': 'gather', 'h4435': 'gauge', 'h4436': 'gaze', 'h4441': 'general',
            'h4442': 'genius', 'h4443': 'genre', 'h4444': 'gentle', 'h4445': 'genuine', 'h4446': 'gesture',
            'h4451': 'ghost', 'h4452': 'giant', 'h4453': 'gift', 'h4454': 'giggle', 'h4455': 'ginger',
            'h4456': 'giraffe', 'h4461': 'girl', 'h4462': 'give', 'h4463': 'glad', 'h4464': 'glance', 'h4465': 'glare',
            'h4466': 'glass', 'h4511': 'glide', 'h4512': 'glimpse', 'h4513': 'globe', 'h4514': 'gloom',
            'h4515': 'glory', 'h4516': 'glove', 'h4521': 'glow', 'h4522': 'glue', 'h4523': 'goat', 'h4524': 'goddess',
            'h4525': 'gold', 'h4526': 'good', 'h4531': 'goose', 'h4532': 'gorilla', 'h4533': 'gospel',
            'h4534': 'gossip', 'h4535': 'govern', 'h4536': 'gown', 'h4541': 'grab', 'h4542': 'grace', 'h4543': 'grain',
            'h4544': 'grant', 'h4545': 'grape', 'h4546': 'grass', 'h4551': 'gravity', 'h4552': 'great',
            'h4553': 'green', 'h4554': 'grid', 'h4555': 'grief', 'h4556': 'grit', 'h4561': 'grocery', 'h4562': 'group',
            'h4563': 'grow', 'h4564': 'grunt', 'h4565': 'guard', 'h4566': 'guess', 'h4611': 'guide', 'h4612': 'guilt',
            'h4613': 'guitar', 'h4614': 'gun', 'h4615': 'gym', 'h4616': 'habit', 'h4621': 'hair', 'h4622': 'half',
            'h4623': 'hammer', 'h4624': 'hamster', 'h4625': 'hand', 'h4626': 'happy', 'h4631': 'harbor',
            'h4632': 'hard', 'h4633': 'harsh', 'h4634': 'harvest', 'h4635': 'hat', 'h4636': 'have', 'h4641': 'hawk',
            'h4642': 'hazard', 'h4643': 'head', 'h4644': 'health', 'h4645': 'heart', 'h4646': 'heavy',
            'h4651': 'hedgehog', 'h4652': 'height', 'h4653': 'hello', 'h4654': 'helmet', 'h4655': 'help',
            'h4656': 'hen', 'h4661': 'hero', 'h4662': 'hidden', 'h4663': 'high', 'h4664': 'hill', 'h4665': 'hint',
            'h4666': 'hip', 'h5111': 'hire', 'h5112': 'history', 'h5113': 'hobby', 'h5114': 'hockey', 'h5115': 'hold',
            'h5116': 'hole', 'h5121': 'holiday', 'h5122': 'hollow', 'h5123': 'home', 'h5124': 'honey', 'h5125': 'hood',
            'h5126': 'hope', 'h5131': 'horn', 'h5132': 'horror', 'h5133': 'horse', 'h5134': 'hospital', 'h5135': 'host',
            'h5136': 'hotel', 'h5141': 'hour', 'h5142': 'hover', 'h5143': 'hub', 'h5144': 'huge', 'h5145': 'human',
            'h5146': 'humble', 'h5151': 'humor', 'h5152': 'hundred', 'h5153': 'hungry', 'h5154': 'hunt',
            'h5155': 'hurdle', 'h5156': 'hurry', 'h5161': 'hurt', 'h5162': 'husband', 'h5163': 'hybrid', 'h5164': 'ice',
            'h5165': 'icon', 'h5166': 'idea', 'h5211': 'identify', 'h5212': 'idle', 'h5213': 'ignore', 'h5214': 'ill',
            'h5215': 'illegal', 'h5216': 'illness', 'h5221': 'image', 'h5222': 'imitate', 'h5223': 'immense',
            'h5224': 'immune', 'h5225': 'impact', 'h5226': 'impose', 'h5231': 'improve', 'h5232': 'impulse',
            'h5233': 'inch', 'h5234': 'include', 'h5235': 'income', 'h5236': 'increase', 'h5241': 'index',
            'h5242': 'indicate', 'h5243': 'indoor', 'h5244': 'industry', 'h5245': 'infant', 'h5246': 'inflict',
            'h5251': 'inform', 'h5252': 'inhale', 'h5253': 'inherit', 'h5254': 'initial', 'h5255': 'inject',
            'h5256': 'injury', 'h5261': 'inmate', 'h5262': 'inner', 'h5263': 'innocent', 'h5264': 'input',
            'h5265': 'inquiry', 'h5266': 'insane', 'h5311': 'insect', 'h5312': 'inside', 'h5313': 'inspire',
            'h5314': 'install', 'h5315': 'intact', 'h5316': 'interest', 'h5321': 'into', 'h5322': 'invest',
            'h5323': 'invite', 'h5324': 'involve', 'h5325': 'iron', 'h5326': 'island', 'h5331': 'isolate',
            'h5332': 'issue', 'h5333': 'item', 'h5334': 'ivory', 'h5335': 'jacket', 'h5336': 'jaguar', 'h5341': 'jar',
            'h5342': 'jazz', 'h5343': 'jealous', 'h5344': 'jeans', 'h5345': 'jelly', 'h5346': 'jewel', 'h5351': 'job',
            'h5352': 'join', 'h5353': 'joke', 'h5354': 'journey', 'h5355': 'joy', 'h5356': 'judge', 'h5361': 'juice',
            'h5362': 'jump', 'h5363': 'jungle', 'h5364': 'junior', 'h5365': 'junk', 'h5366': 'just',
            'h5411': 'kangaroo', 'h5412': 'keen', 'h5413': 'keep', 'h5414': 'ketchup', 'h5415': 'key', 'h5416': 'kick',
            'h5421': 'kid', 'h5422': 'kidney', 'h5423': 'kind', 'h5424': 'kingdom', 'h5425': 'kiss', 'h5426': 'kit',
            'h5431': 'kitchen', 'h5432': 'kite', 'h5433': 'kitten', 'h5434': 'kiwi', 'h5435': 'knee', 'h5436': 'knife',
            'h5441': 'knock', 'h5442': 'know', 'h5443': 'lab', 'h5444': 'label', 'h5445': 'labor', 'h5446': 'ladder',
            'h5451': 'lady', 'h5452': 'lake', 'h5453': 'lamp', 'h5454': 'language', 'h5455': 'laptop', 'h5456': 'large',
            'h5461': 'later', 'h5462': 'latin', 'h5463': 'laugh', 'h5464': 'laundry', 'h5465': 'lava', 'h5466': 'law',
            'h5511': 'lawn', 'h5512': 'lawsuit', 'h5513': 'layer', 'h5514': 'lazy', 'h5515': 'leader', 'h5516': 'leaf',
            'h5521': 'learn', 'h5522': 'leave', 'h5523': 'lecture', 'h5524': 'left', 'h5525': 'leg', 'h5526': 'legal',
            'h5531': 'legend', 'h5532': 'leisure', 'h5533': 'lemon', 'h5534': 'lend', 'h5535': 'length',
            'h5536': 'lens', 'h5541': 'leopard', 'h5542': 'lesson', 'h5543': 'letter', 'h5544': 'level',
            'h5545': 'liar', 'h5546': 'liberty', 'h5551': 'library', 'h5552': 'license', 'h5553': 'life',
            'h5554': 'lift', 'h5555': 'light', 'h5556': 'like', 'h5561': 'limb', 'h5562': 'limit', 'h5563': 'link',
            'h5564': 'lion', 'h5565': 'liquid', 'h5566': 'list', 'h5611': 'little', 'h5612': 'live', 'h5613': 'lizard',
            'h5614': 'load', 'h5615': 'loan', 'h5616': 'lobster', 'h5621': 'local', 'h5622': 'lock', 'h5623': 'logic',
            'h5624': 'lonely', 'h5625': 'long', 'h5626': 'loop', 'h5631': 'lottery', 'h5632': 'loud', 'h5633': 'lounge',
            'h5634': 'love', 'h5635': 'loyal', 'h5636': 'lucky', 'h5641': 'luggage', 'h5642': 'lumber',
            'h5643': 'lunar', 'h5644': 'lunch', 'h5645': 'luxury', 'h5646': 'lyrics', 'h5651': 'machine',
            'h5652': 'mad', 'h5653': 'magic', 'h5654': 'magnet', 'h5655': 'maid', 'h5656': 'mail', 'h5661': 'main',
            'h5662': 'major', 'h5663': 'make', 'h5664': 'mammal', 'h5665': 'man', 'h5666': 'manage', 'h6111': 'mandate',
            'h6112': 'mango', 'h6113': 'mansion', 'h6114': 'manual', 'h6115': 'maple', 'h6116': 'marble',
            'h6121': 'march', 'h6122': 'margin', 'h6123': 'marine', 'h6124': 'market', 'h6125': 'marriage',
            'h6126': 'mask', 'h6131': 'mass', 'h6132': 'master', 'h6133': 'match', 'h6134': 'material', 'h6135': 'math',
            'h6136': 'matrix', 'h6141': 'matter', 'h6142': 'maximum', 'h6143': 'maze', 'h6144': 'meadow',
            'h6145': 'mean', 'h6146': 'measure', 'h6151': 'meat', 'h6152': 'mechanic', 'h6153': 'medal',
            'h6154': 'media', 'h6155': 'melody', 'h6156': 'melt', 'h6161': 'member', 'h6162': 'memory',
            'h6163': 'mention', 'h6164': 'menu', 'h6165': 'mercy', 'h6166': 'merge', 'h6211': 'merit', 'h6212': 'merry',
            'h6213': 'mesh', 'h6214': 'message', 'h6215': 'metal', 'h6216': 'method', 'h6221': 'middle',
            'h6222': 'midnight', 'h6223': 'milk', 'h6224': 'million', 'h6225': 'mimic', 'h6226': 'mind',
            'h6231': 'minimum', 'h6232': 'minor', 'h6233': 'minute', 'h6234': 'miracle', 'h6235': 'mirror',
            'h6236': 'misery', 'h6241': 'miss', 'h6242': 'mistake', 'h6243': 'mix', 'h6244': 'mixed',
            'h6245': 'mixture', 'h6246': 'mobile', 'h6251': 'model', 'h6252': 'modify', 'h6253': 'mom',
            'h6254': 'moment', 'h6255': 'monitor', 'h6256': 'monkey', 'h6261': 'monster', 'h6262': 'month',
            'h6263': 'moon', 'h6264': 'moral', 'h6265': 'more', 'h6266': 'morning', 'h6311': 'mosquito',
            'h6312': 'mother', 'h6313': 'motion', 'h6314': 'motor', 'h6315': 'mountain', 'h6316': 'mouse',
            'h6321': 'move', 'h6322': 'movie', 'h6323': 'much', 'h6324': 'muffin', 'h6325': 'mule', 'h6326': 'multiply',
            'h6331': 'muscle', 'h6332': 'museum', 'h6333': 'mushroom', 'h6334': 'music', 'h6335': 'must',
            'h6336': 'mutual', 'h6341': 'myself', 'h6342': 'mystery', 'h6343': 'myth', 'h6344': 'naive',
            'h6345': 'name', 'h6346': 'napkin', 'h6351': 'narrow', 'h6352': 'nasty', 'h6353': 'nation',
            'h6354': 'nature', 'h6355': 'near', 'h6356': 'neck', 'h6361': 'need', 'h6362': 'negative',
            'h6363': 'neglect', 'h6364': 'neither', 'h6365': 'nephew', 'h6366': 'nerve', 'h6411': 'nest',
            'h6412': 'net', 'h6413': 'network', 'h6414': 'neutral', 'h6415': 'never', 'h6416': 'news', 'h6421': 'next',
            'h6422': 'nice', 'h6423': 'night', 'h6424': 'noble', 'h6425': 'noise', 'h6426': 'nominee',
            'h6431': 'noodle', 'h6432': 'normal', 'h6433': 'north', 'h6434': 'nose', 'h6435': 'notable',
            'h6436': 'note', 'h6441': 'nothing', 'h6442': 'notice', 'h6443': 'novel', 'h6444': 'now',
            'h6445': 'nuclear', 'h6446': 'number', 'h6451': 'nurse', 'h6452': 'nut', 'h6453': 'oak', 'h6454': 'obey',
            'h6455': 'object', 'h6456': 'oblige', 'h6461': 'obscure', 'h6462': 'observe', 'h6463': 'obtain',
            'h6464': 'obvious', 'h6465': 'occur', 'h6466': 'ocean', 'h6511': 'october', 'h6512': 'odor', 'h6513': 'off',
            'h6514': 'offer', 'h6515': 'office', 'h6516': 'often', 'h6521': 'oil', 'h6522': 'okay', 'h6523': 'old',
            'h6524': 'olive', 'h6525': 'olympic', 'h6526': 'omit', 'h6531': 'once', 'h6532': 'one', 'h6533': 'onion',
            'h6534': 'online', 'h6535': 'only', 'h6536': 'open', 'h6541': 'opera', 'h6542': 'opinion',
            'h6543': 'oppose', 'h6544': 'option', 'h6545': 'orange', 'h6546': 'orbit', 'h6551': 'orchard',
            'h6552': 'order', 'h6553': 'ordinary', 'h6554': 'organ', 'h6555': 'orient', 'h6556': 'original',
            'h6561': 'orphan', 'h6562': 'ostrich', 'h6563': 'other', 'h6564': 'outdoor', 'h6565': 'outer',
            'h6566': 'output', 'h6611': 'outside', 'h6612': 'oval', 'h6613': 'oven', 'h6614': 'over', 'h6615': 'own',
            'h6616': 'owner', 'h6621': 'oxygen', 'h6622': 'oyster', 'h6623': 'ozone', 'h6624': 'pact',
            'h6625': 'paddle', 'h6626': 'page', 'h6631': 'pair', 'h6632': 'palace', 'h6633': 'palm', 'h6634': 'panda',
            'h6635': 'panel', 'h6636': 'panic', 'h6641': 'panther', 'h6642': 'paper', 'h6643': 'parade',
            'h6644': 'parent', 'h6645': 'park', 'h6646': 'parrot', 'h6651': 'party', 'h6652': 'pass', 'h6653': 'patch',
            'h6654': 'path', 'h6655': 'patient', 'h6656': 'patrol', 'h6661': 'pattern', 'h6662': 'pause',
            'h6663': 'pave', 'h6664': 'payment', 'h6665': 'peace', 'h6666': 'peanut', 't1111': 'pear',
            't1112': 'peasant', 't1113': 'pelican', 't1114': 'pen', 't1115': 'penalty', 't1116': 'pencil',
            't1121': 'people', 't1122': 'pepper', 't1123': 'perfect', 't1124': 'permit', 't1125': 'person',
            't1126': 'pet', 't1131': 'phone', 't1132': 'photo', 't1133': 'phrase', 't1134': 'physical',
            't1135': 'piano', 't1136': 'picnic', 't1141': 'picture', 't1142': 'piece', 't1143': 'pig',
            't1144': 'pigeon', 't1145': 'pill', 't1146': 'pilot', 't1151': 'pink', 't1152': 'pioneer', 't1153': 'pipe',
            't1154': 'pistol', 't1155': 'pitch', 't1156': 'pizza', 't1161': 'place', 't1162': 'planet',
            't1163': 'plastic', 't1164': 'plate', 't1165': 'play', 't1166': 'please', 't1211': 'pledge',
            't1212': 'pluck', 't1213': 'plug', 't1214': 'plunge', 't1215': 'poem', 't1216': 'poet', 't1221': 'point',
            't1222': 'polar', 't1223': 'pole', 't1224': 'police', 't1225': 'pond', 't1226': 'pony', 't1231': 'pool',
            't1232': 'popular', 't1233': 'portion', 't1234': 'position', 't1235': 'possible', 't1236': 'post',
            't1241': 'potato', 't1242': 'pottery', 't1243': 'poverty', 't1244': 'powder', 't1245': 'power',
            't1246': 'practice', 't1251': 'praise', 't1252': 'predict', 't1253': 'prefer', 't1254': 'prepare',
            't1255': 'present', 't1256': 'pretty', 't1261': 'prevent', 't1262': 'price', 't1263': 'pride',
            't1264': 'primary', 't1265': 'print', 't1266': 'priority', 't1311': 'prison', 't1312': 'private',
            't1313': 'prize', 't1314': 'problem', 't1315': 'process', 't1316': 'produce', 't1321': 'profit',
            't1322': 'program', 't1323': 'project', 't1324': 'promote', 't1325': 'proof', 't1326': 'property',
            't1331': 'prosper', 't1332': 'protect', 't1333': 'proud', 't1334': 'provide', 't1335': 'public',
            't1336': 'pudding', 't1341': 'pull', 't1342': 'pulp', 't1343': 'pulse', 't1344': 'pumpkin',
            't1345': 'punch', 't1346': 'pupil', 't1351': 'puppy', 't1352': 'purchase', 't1353': 'purity',
            't1354': 'purpose', 't1355': 'purse', 't1356': 'push', 't1361': 'put', 't1362': 'puzzle',
            't1363': 'pyramid', 't1364': 'quality', 't1365': 'quantum', 't1366': 'quarter', 't1411': 'question',
            't1412': 'quick', 't1413': 'quit', 't1414': 'quiz', 't1415': 'quote', 't1416': 'rabbit', 't1421': 'raccoon',
            't1422': 'race', 't1423': 'rack', 't1424': 'radar', 't1425': 'radio', 't1426': 'rail', 't1431': 'rain',
            't1432': 'raise', 't1433': 'rally', 't1434': 'ramp', 't1435': 'ranch', 't1436': 'random', 't1441': 'range',
            't1442': 'rapid', 't1443': 'rare', 't1444': 'rate', 't1445': 'rather', 't1446': 'raven', 't1451': 'raw',
            't1452': 'razor', 't1453': 'ready', 't1454': 'real', 't1455': 'reason', 't1456': 'rebel',
            't1461': 'rebuild', 't1462': 'recall', 't1463': 'receive', 't1464': 'recipe', 't1465': 'record',
            't1466': 'recycle', 't1511': 'reduce', 't1512': 'reflect', 't1513': 'reform', 't1514': 'refuse',
            't1515': 'region', 't1516': 'regret', 't1521': 'regular', 't1522': 'reject', 't1523': 'relax',
            't1524': 'release', 't1525': 'relief', 't1526': 'rely', 't1531': 'remain', 't1532': 'remember',
            't1533': 'remind', 't1534': 'remove', 't1535': 'render', 't1536': 'renew', 't1541': 'rent',
            't1542': 'reopen', 't1543': 'repair', 't1544': 'repeat', 't1545': 'replace', 't1546': 'report',
            't1551': 'require', 't1552': 'rescue', 't1553': 'resemble', 't1554': 'resist', 't1555': 'resource',
            't1556': 'response', 't1561': 'result', 't1562': 'retire', 't1563': 'retreat', 't1564': 'return',
            't1565': 'reunion', 't1566': 'reveal', 't1611': 'review', 't1612': 'reward', 't1613': 'rhythm',
            't1614': 'rib', 't1615': 'ribbon', 't1616': 'rice', 't1621': 'rich', 't1622': 'ride', 't1623': 'ridge',
            't1624': 'rifle', 't1625': 'right', 't1626': 'rigid', 't1631': 'ring', 't1632': 'riot', 't1633': 'ripple',
            't1634': 'risk', 't1635': 'ritual', 't1636': 'rival', 't1641': 'river', 't1642': 'road', 't1643': 'roast',
            't1644': 'robot', 't1645': 'robust', 't1646': 'rocket', 't1651': 'romance', 't1652': 'roof',
            't1653': 'rookie', 't1654': 'room', 't1655': 'rose', 't1656': 'rotate', 't1661': 'rough', 't1662': 'round',
            't1663': 'route', 't1664': 'royal', 't1665': 'rubber', 't1666': 'rude', 't2111': 'rug', 't2112': 'rule',
            't2113': 'run', 't2114': 'runway', 't2115': 'rural', 't2116': 'sad', 't2121': 'saddle', 't2122': 'sadness',
            't2123': 'safe', 't2124': 'sail', 't2125': 'salad', 't2126': 'salmon', 't2131': 'salon', 't2132': 'salt',
            't2133': 'salute', 't2134': 'same', 't2135': 'sample', 't2136': 'sand', 't2141': 'satisfy',
            't2142': 'satoshi', 't2143': 'sauce', 't2144': 'sausage', 't2145': 'save', 't2146': 'say', 't2151': 'scale',
            't2152': 'scan', 't2153': 'scare', 't2154': 'scatter', 't2155': 'scene', 't2156': 'scheme',
            't2161': 'school', 't2162': 'science', 't2163': 'scissors', 't2164': 'scorpion', 't2165': 'scout',
            't2166': 'scrap', 't2211': 'screen', 't2212': 'script', 't2213': 'scrub', 't2214': 'sea', 't2215': 'search',
            't2216': 'season', 't2221': 'seat', 't2222': 'second', 't2223': 'secret', 't2224': 'section',
            't2225': 'security', 't2226': 'seed', 't2231': 'seek', 't2232': 'segment', 't2233': 'select',
            't2234': 'sell', 't2235': 'seminar', 't2236': 'senior', 't2241': 'sense', 't2242': 'sentence',
            't2243': 'series', 't2244': 'service', 't2245': 'session', 't2246': 'settle', 't2251': 'setup',
            't2252': 'seven', 't2253': 'shadow', 't2254': 'shaft', 't2255': 'shallow', 't2256': 'share',
            't2261': 'shed', 't2262': 'shell', 't2263': 'sheriff', 't2264': 'shield', 't2265': 'shift',
            't2266': 'shine', 't2311': 'ship', 't2312': 'shiver', 't2313': 'shock', 't2314': 'shoe', 't2315': 'shoot',
            't2316': 'shop', 't2321': 'short', 't2322': 'shoulder', 't2323': 'shove', 't2324': 'shrimp',
            't2325': 'shrug', 't2326': 'shuffle', 't2331': 'shy', 't2332': 'sibling', 't2333': 'sick', 't2334': 'side',
            't2335': 'siege', 't2336': 'sight', 't2341': 'sign', 't2342': 'silent', 't2343': 'silk', 't2344': 'silly',
            't2345': 'silver', 't2346': 'similar', 't2351': 'simple', 't2352': 'since', 't2353': 'sing',
            't2354': 'siren', 't2355': 'sister', 't2356': 'situate', 't2361': 'six', 't2362': 'size', 't2363': 'skate',
            't2364': 'sketch', 't2365': 'ski', 't2366': 'skill', 't2411': 'skin', 't2412': 'skirt', 't2413': 'skull',
            't2414': 'slab', 't2415': 'slam', 't2416': 'sleep', 't2421': 'slender', 't2422': 'slice', 't2423': 'slide',
            't2424': 'slight', 't2425': 'slim', 't2426': 'slogan', 't2431': 'slot', 't2432': 'slow', 't2433': 'slush',
            't2434': 'small', 't2435': 'smart', 't2436': 'smile', 't2441': 'smoke', 't2442': 'smooth', 't2443': 'snack',
            't2444': 'snake', 't2445': 'snap', 't2446': 'sniff', 't2451': 'snow', 't2452': 'soap', 't2453': 'soccer',
            't2454': 'social', 't2455': 'sock', 't2456': 'soda', 't2461': 'soft', 't2462': 'solar', 't2463': 'soldier',
            't2464': 'solid', 't2465': 'solution', 't2466': 'solve', 't2511': 'someone', 't2512': 'song',
            't2513': 'soon', 't2514': 'sorry', 't2515': 'sort', 't2516': 'soul', 't2521': 'sound', 't2522': 'soup',
            't2523': 'source', 't2524': 'south', 't2525': 'space', 't2526': 'spare', 't2531': 'spatial',
            't2532': 'spawn', 't2533': 'speak', 't2534': 'special', 't2535': 'speed', 't2536': 'spell',
            't2541': 'spend', 't2542': 'sphere', 't2543': 'spice', 't2544': 'spider', 't2545': 'spike', 't2546': 'spin',
            't2551': 'spirit', 't2552': 'split', 't2553': 'spoil', 't2554': 'sponsor', 't2555': 'spoon',
            't2556': 'sport', 't2561': 'spot', 't2562': 'spray', 't2563': 'spread', 't2564': 'spring', 't2565': 'spy',
            't2566': 'square', 't2611': 'squeeze', 't2612': 'squirrel', 't2613': 'stable', 't2614': 'stadium',
            't2615': 'staff', 't2616': 'stage', 't2621': 'stairs', 't2622': 'stamp', 't2623': 'stand', 't2624': 'start',
            't2625': 'state', 't2626': 'stay', 't2631': 'steak', 't2632': 'steel', 't2633': 'stem', 't2634': 'step',
            't2635': 'stereo', 't2636': 'stick', 't2641': 'still', 't2642': 'sting', 't2643': 'stock',
            't2644': 'stomach', 't2645': 'stone', 't2646': 'stool', 't2651': 'story', 't2652': 'stove',
            't2653': 'strategy', 't2654': 'street', 't2655': 'strike', 't2656': 'strong', 't2661': 'struggle',
            't2662': 'student', 't2663': 'stuff', 't2664': 'stumble', 't2665': 'style', 't2666': 'subject',
            't3111': 'submit', 't3112': 'subway', 't3113': 'success', 't3114': 'such', 't3115': 'sudden',
            't3116': 'suffer', 't3121': 'sugar', 't3122': 'suggest', 't3123': 'suit', 't3124': 'summer', 't3125': 'sun',
            't3126': 'sunny', 't3131': 'sunset', 't3132': 'super', 't3133': 'supply', 't3134': 'supreme',
            't3135': 'sure', 't3136': 'surface', 't3141': 'surge', 't3142': 'surprise', 't3143': 'surround',
            't3144': 'survey', 't3145': 'suspect', 't3146': 'sustain', 't3151': 'swallow', 't3152': 'swamp',
            't3153': 'swap', 't3154': 'swarm', 't3155': 'swear', 't3156': 'sweet', 't3161': 'swift', 't3162': 'swim',
            't3163': 'swing', 't3164': 'switch', 't3165': 'sword', 't3166': 'symbol', 't3211': 'symptom',
            't3212': 'syrup', 't3213': 'system', 't3214': 'table', 't3215': 'tackle', 't3216': 'tag', 't3221': 'tail',
            't3222': 'talent', 't3223': 'talk', 't3224': 'tank', 't3225': 'tape', 't3226': 'target', 't3231': 'task',
            't3232': 'taste', 't3233': 'tattoo', 't3234': 'taxi', 't3235': 'teach', 't3236': 'team', 't3241': 'tell',
            't3242': 'ten', 't3243': 'tenant', 't3244': 'tennis', 't3245': 'tent', 't3246': 'term', 't3251': 'test',
            't3252': 'text', 't3253': 'thank', 't3254': 'that', 't3255': 'theme', 't3256': 'then', 't3261': 'theory',
            't3262': 'there', 't3263': 'they', 't3264': 'thing', 't3265': 'this', 't3266': 'thought', 't3311': 'three',
            't3312': 'thrive', 't3313': 'throw', 't3314': 'thumb', 't3315': 'thunder', 't3316': 'ticket',
            't3321': 'tide', 't3322': 'tiger', 't3323': 'tilt', 't3324': 'timber', 't3325': 'time', 't3326': 'tiny',
            't3331': 'tip', 't3332': 'tired', 't3333': 'tissue', 't3334': 'title', 't3335': 'toast', 't3336': 'tobacco',
            't3341': 'today', 't3342': 'toddler', 't3343': 'toe', 't3344': 'together', 't3345': 'toilet',
            't3346': 'token', 't3351': 'tomato', 't3352': 'tomorrow', 't3353': 'tone', 't3354': 'tongue',
            't3355': 'tonight', 't3356': 'tool', 't3361': 'tooth', 't3362': 'top', 't3363': 'topic', 't3364': 'topple',
            't3365': 'torch', 't3366': 'tornado', 't3411': 'tortoise', 't3412': 'toss', 't3413': 'total',
            't3414': 'tourist', 't3415': 'toward', 't3416': 'tower', 't3421': 'town', 't3422': 'toy', 't3423': 'track',
            't3424': 'trade', 't3425': 'traffic', 't3426': 'tragic', 't3431': 'train', 't3432': 'transfer',
            't3433': 'trap', 't3434': 'trash', 't3435': 'travel', 't3436': 'tray', 't3441': 'treat', 't3442': 'tree',
            't3443': 'trend', 't3444': 'trial', 't3445': 'tribe', 't3446': 'trick', 't3451': 'trigger', 't3452': 'trim',
            't3453': 'trip', 't3454': 'trophy', 't3455': 'trouble', 't3456': 'truck', 't3461': 'true', 't3462': 'truly',
            't3463': 'trumpet', 't3464': 'trust', 't3465': 'truth', 't3466': 'try', 't3511': 'tube', 't3512': 'tuition',
            't3513': 'tumble', 't3514': 'tuna', 't3515': 'tunnel', 't3516': 'turkey', 't3521': 'turn',
            't3522': 'turtle', 't3523': 'twelve', 't3524': 'twenty', 't3525': 'twice', 't3526': 'twin',
            't3531': 'twist', 't3532': 'two', 't3533': 'type', 't3534': 'typical', 't3535': 'ugly', 't3536': 'umbrella',
            't3541': 'unable', 't3542': 'unaware', 't3543': 'uncle', 't3544': 'uncover', 't3545': 'under',
            't3546': 'undo', 't3551': 'unfair', 't3552': 'unfold', 't3553': 'unhappy', 't3554': 'uniform',
            't3555': 'unique', 't3556': 'unit', 't3561': 'universe', 't3562': 'unknown', 't3563': 'unlock',
            't3564': 'until', 't3565': 'unusual', 't3566': 'unveil', 't3611': 'update', 't3612': 'upgrade',
            't3613': 'uphold', 't3614': 'upon', 't3615': 'upper', 't3616': 'upset', 't3621': 'urban', 't3622': 'urge',
            't3623': 'usage', 't3624': 'use', 't3625': 'used', 't3626': 'useful', 't3631': 'useless', 't3632': 'usual',
            't3633': 'utility', 't3634': 'vacant', 't3635': 'vacuum', 't3636': 'vague', 't3641': 'valid',
            't3642': 'valley', 't3643': 'valve', 't3644': 'van', 't3645': 'vanish', 't3646': 'vapor',
            't3651': 'various', 't3652': 'vast', 't3653': 'vault', 't3654': 'vehicle', 't3655': 'velvet',
            't3656': 'vendor', 't3661': 'venture', 't3662': 'venue', 't3663': 'verb', 't3664': 'verify',
            't3665': 'version', 't3666': 'very', 't4111': 'vessel', 't4112': 'veteran', 't4113': 'viable',
            't4114': 'vibrant', 't4115': 'vicious', 't4116': 'victory', 't4121': 'video', 't4122': 'view',
            't4123': 'village', 't4124': 'vintage', 't4125': 'violin', 't4126': 'virtual', 't4131': 'virus',
            't4132': 'visa', 't4133': 'visit', 't4134': 'visual', 't4135': 'vital', 't4136': 'vivid', 't4141': 'vocal',
            't4142': 'voice', 't4143': 'void', 't4144': 'volcano', 't4145': 'volume', 't4146': 'vote',
            't4151': 'voyage', 't4152': 'wage', 't4153': 'wagon', 't4154': 'wait', 't4155': 'walk', 't4156': 'wall',
            't4161': 'walnut', 't4162': 'want', 't4163': 'warfare', 't4164': 'warm', 't4165': 'warrior',
            't4166': 'wash', 't4211': 'wasp', 't4212': 'waste', 't4213': 'water', 't4214': 'wave', 't4215': 'way',
            't4216': 'wealth', 't4221': 'weapon', 't4222': 'wear', 't4223': 'weasel', 't4224': 'weather',
            't4225': 'web', 't4226': 'wedding', 't4231': 'weekend', 't4232': 'weird', 't4233': 'welcome',
            't4234': 'west', 't4235': 'wet', 't4236': 'whale', 't4241': 'what', 't4242': 'wheat', 't4243': 'wheel',
            't4244': 'when', 't4245': 'where', 't4246': 'whip', 't4251': 'whisper', 't4252': 'wide', 't4253': 'width',
            't4254': 'wife', 't4255': 'wild', 't4256': 'will', 't4261': 'win', 't4262': 'window', 't4263': 'wine',
            't4264': 'wing', 't4265': 'wink', 't4266': 'winner', 't4311': 'winter', 't4312': 'wire', 't4313': 'wisdom',
            't4314': 'wise', 't4315': 'wish', 't4316': 'witness', 't4321': 'wolf', 't4322': 'woman', 't4323': 'wonder',
            't4324': 'wood', 't4325': 'wool', 't4326': 'word', 't4331': 'work', 't4332': 'world', 't4333': 'worry',
            't4334': 'worth', 't4335': 'wrap', 't4336': 'wreck', 't4341': 'wrestle', 't4342': 'wrist', 't4343': 'write',
            't4344': 'wrong', 't4345': 'yard', 't4346': 'year', 't4351': 'yellow', 't4352': 'you', 't4353': 'young',
            't4354': 'youth', 't4355': 'zebra', 't4356': 'zero', 't4361': 'zone', 't4362': 'zoo'}


def get_bip39():
    s = bip39_roll()
    indexes = get_indexes(s)
    bip39 = list(wordbank.values())
    phraselist = match_words(indexes, bip39)
    final_word = checksum(s, bip39)
    phraselist[-1] = final_word
    bip39phrase = " "
    bip39phrase = bip39phrase.join(phraselist)
    return bip39phrase


def bip39_roll():
    s = ""
    times = 0
    while times < 256:
        n = random.randint(1, 6)
        if n <= 3:
            d = "0"
        else:
            d = "1"
        s = s + d
        times += 1
    return s


def get_indexes(s):
    indexes = []
    i = 0
    while i < 23:
        w = str(int(s[0 + (11 * i):11 + (11 * i)], 2))  # was +1 - I think I was adding twice
        indexes.append(w)
        i += 1
    last_three = s[-3:]
    indexes.append(last_three)
    return indexes


# Get wordbank removed (was duplicated)


def match_words(indexes, bip39):
    phrase = []
    for index in indexes:
        word = bip39[int(index)]
        phrase.append(word)
        # phrase = phrase+" "+word # return a list instead
    return phrase


def checksum(s, bip39):
    # String of binary to actual bytes
    zz = int(s, 2).to_bytes(len(s) // 8, byteorder="big")

    # Hash it
    h = hashlib.sha256(zz).hexdigest()

    # The first two digits of the hash, then to binary of them
    f = get_letter_number(h[0])
    ss = get_letter_number(h[1])
    fb = bin(int(f))[2:].zfill(4)
    sb = bin(int(ss))[2:].zfill(4)

    # Add them to the leftovers
    s_last = s[-3:]
    final = s_last + fb + sb

    checksum_word_index = int(final, 2)  # + 1
    final_word = bip39[checksum_word_index]
    return final_word


def get_letter_number(letter):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter in letters:

        # get the NUMBER and then it's the binary NUMBER (I think...)
        letter = letter.lower()
        i = letters.index(letter)
        i = i + 10  # (a=10,b=11, etc.)
        return i
    else:
        return letter  # nothing to see here - send it back!


def first_four(partial_word):
    if len(partial_word) < 4:
        return "Partial word must be at least four characters."
    for word in wordbank.values():
        if partial_word[0:4] == word[0:4]:
            return word
    return "Not found!"


# Just a random extra utility that might be needed
def generate_password(password_length):
    chars = "!#$%&'()*+,-./23456789:;<=>?@ABCDEFGHJKLMNOPRSTUVWXYZ[\]^_abcdefghijkmnopqrstuvwxyz{|}~"
    password = ""
    i = 0
    while i < password_length:
        x = random.randint(0, len(chars) - 1)
        password = password + chars[x]
        i += 1
    return password


if __name__ == '__main__':
    print(get_bip39())
    print(first_four("aban"))
    print(generate_password(16))
