#!/usr/bin/env python
# encoding: utf-8

debug_server = ["http://172.16.42.102:8001/demo/ctrl.php","http://172.16.42.101:8001/demo/ctrl.php","http://172.16.42.103:8001/demo/ctrl.php","http://123.207.86.208:8001/demo/ctrl.php","http://118.89.35.160:8001/demo/ctrl.php"]
debug_server_requests = ["http://172.16.42.102:8001/","http://172.16.42.101:8001/","http://172.16.42.103:8001/","http://123.207.86.208:8001/","http://118.89.35.160:8001/","http://172.16.42.104:8004/","http://116.62.119.39:8001/","http://172.16.42.105:8004/"]
bingtuanId = [101, 102, 103, 104, 105, 106, 107, 201, 202, 203, 204, 205, 206, 207, 301, 302, 303, 304, 305, 306, 307,401, 402, 403, 404, 405, 406, 407, 501, 502, 503, 504, 505, 506, 507, 601, 602, 603, 604, 605, 606, 607,901, 902, 903, 904, 905, 906, 907,701,702,703,704,705,706,707,308]
potentialId = [1, 2, 3]
resource = ['gem', 'gold', 'texp', 'physcal']
bingtuansuipianId = "3101,3102,3103,3104,3105,3106,3107,3201,3202,3203,3204,3205,3206,3207,3301,3302,3303,3304,3305,3306,3307,3401,3402,3403,3404,3405,3406,3407,3501,3502,3503,3504,3505,3506,3507,3601,3602,3603,3604,3605,3606,3607,3901,3902,3903,3904,3905,3906,3907,3701,3702,3703,3704,3705,3706,3707,3308"
jinjiecailiaoId = "301101,301102,301103,301104,301105,301106,301201,301202,301203,301204,301205,301206,301301,301302,301303,301304,301305,301306,301307,301401,301402,301403,301404,301405,301406,301407,301501,301502,301503,301504,301505,301506,301507,301601,301602,301603,301604,301605,301606,301607,301701,301702,301703,301704,301705,301706,301707,301801,301802,301803,301804,301805,301806,301807,301901,301902,301903,301904,301905,301906,301907,302001,302002,302003,302004,302005,302006,302007,302101,302102,302103,302104,302105,302106,302107,302201,302202,302203,302204,302205,302206,302207,302301,302302,302303,302304,302305,302306,302307,302401,302402,302403,302404,302405,302406,302407"
herosuipianId = "360001,360101,360102,360103,360301,360302,360303,360401,360502,360601,360602,360603,360604,360701,360802,360901,361201,361202,360702,361401,361301,360104"
baowustr = "40111,40112,40113,40121,40122,40123,40211,40212,40213,40221,40222,40223,40231,40232,40233,40301,40302,40303,40304,40311,40312,40313,40314,40101,40102,40103,40321,40322,40323,40421,40422,40423,40424,40401,40402,40403,40404,40405,40406,40331,40332,40333,40334"
baowu = [40111, 40112, 40113, 40121, 40122, 40123, 40211, 40212, 40213, 40221, 40222, 40223, 40231, 40232, 40233, 40301,40302, 40303, 40304, 40311, 40312, 40313, 40314, 40101, 40102, 40103, 40321, 40322, 40323, 40421, 40422, 40423,40424, 40401, 40402, 40403, 40404, 40405, 40406,40331,40332,40333,40334]
otheritem = "41001,41002,3026,3027,3028,3029,3030,3036,3037,3038,3039,3040,3043,3044,3045,3046,3047,3048,3049,3050,3004,3002,3001,3011,310001"
heroId = [60001, 60101, 60102, 60103, 60301, 60302, 60303, 60401, 60502, 60601, 60602, 60603, 60604, 60701, 60802, 60901, 61201, 61202,60702,60104,61301,61401]
skillposition = [1, 2, 3, 4]
bingtuanId1star = [101, 102, 105, 106, 301, 401, 403, 501, 601, 901,701]
bingtuanId2star = [104, 201, 202, 203, 204, 302, 402, 404, 502, 504, 506, 602, 603, 902, 903,702,703,]
bingtuanId3star = [103, 107, 205, 206, 207, 303, 304, 305, 306, 307, 405, 406, 407, 503, 505, 507, 604, 605, 606, 607,904, 905, 906, 907,707,705,704,706,308]
fashusuipian = "500201,500202,500203,500204,500205,500206,500207,500208,500209,500210,500211,500212,500213,500214,500215,500216,500217,500301,500302,500303,500304,500305,500306,500307,500308,500309,500310,500311,500312,500313,500314,500315,500316,500317,500318,500401,500402,500403,500404,500405,500406,500407,500408,500409,500410,500411,500412,500413,500414,500415,500501,500502,500503,500504,500505,500506,500507,500508,500509,500510,500511,500512,500513,500514,500515,500516,500517,500518,500519"
skillId_all = [201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519]
skillId = [201, 202, 203, 205, 206, 207, 208, 210, 211, 212, 214, 217, 301, 302, 303, 304, 305, 306, 307, 308, 309, 311, 314, 315, 316, 401, 402, 403, 404, 409, 411, 412, 413, 414, 415, 501, 502, 503, 504, 506, 507, 508, 510, 511, 512, 513, 514, 515]
magicTalent = [61011, 61012, 61013, 61021, 61022, 61023, 61031, 61032, 61033, 61040, 62011, 62012, 62013, 62021, 62022, 62023, 62031, 62032, 62033, 62040, 63011, 63012, 63013, 63021, 63022, 63023, 63031, 63032, 63033, 63040, 64011, 64012, 64013, 64021, 64022, 64023, 64031, 64032, 64033, 64040, 65011, 65012, 65013, 65021, 65022, 65023, 65031, 65032, 65033, 65040, 66011, 66012, 66013, 66021, 66022, 66023, 66031, 66032, 66033, 66040]
activateAwaking = [101,106,306,907,301,304,203,204]
