import unittest
import fibs


class TestFibs(unittest.TestCase):

    def setUp(self):
        self.first_301_fibs = [
            0,
            1,
            1,
            2,
            3,
            5,
            8,
            13,
            21,
            34,
            55,
            89,
            144,
            233,
            377,
            610,
            987,
            1597,
            2584,
            4181,
            6765,
            10946,
            17711,
            28657,
            46368,
            75025,
            121393,
            196418,
            317811,
            514229,
            832040,
            1346269,
            2178309,
            3524578,
            5702887,
            9227465,
            14930352,
            24157817,
            39088169,
            63245986,
            102334155,
            165580141,
            267914296,
            433494437,
            701408733,
            1134903170,
            1836311903,
            2971215073,
            4807526976,
            7778742049,
            12586269025,
            20365011074,
            32951280099,
            53316291173,
            86267571272,
            139583862445,
            225851433717,
            365435296162,
            591286729879,
            956722026041,
            1548008755920,
            2504730781961,
            4052739537881,
            6557470319842,
            10610209857723,
            17167680177565,
            27777890035288,
            44945570212853,
            72723460248141,
            117669030460994,
            190392490709135,
            308061521170129,
            498454011879264,
            806515533049393,
            1304969544928657,
            2111485077978050,
            3416454622906707,
            5527939700884757,
            8944394323791464,
            14472334024676221,
            23416728348467685,
            37889062373143906,
            61305790721611591,
            99194853094755497,
            160500643816367088,
            259695496911122585,
            420196140727489673,
            679891637638612258,
            1100087778366101931,
            1779979416004714189,
            2880067194370816120,
            4660046610375530309,
            7540113804746346429,
            12200160415121876738,
            19740274219868223167,
            31940434634990099905,
            51680708854858323072,
            83621143489848422977,
            135301852344706746049,
            218922995834555169026,
            354224848179261915075,
            573147844013817084101,
            927372692193078999176,
            1500520536206896083277,
            2427893228399975082453,
            3928413764606871165730,
            6356306993006846248183,
            10284720757613717413913,
            16641027750620563662096,
            26925748508234281076009,
            43566776258854844738105,
            70492524767089125814114,
            114059301025943970552219,
            184551825793033096366333,
            298611126818977066918552,
            483162952612010163284885,
            781774079430987230203437,
            1264937032042997393488322,
            2046711111473984623691759,
            3311648143516982017180081,
            5358359254990966640871840,
            8670007398507948658051921,
            14028366653498915298923761,
            22698374052006863956975682,
            36726740705505779255899443,
            59425114757512643212875125,
            96151855463018422468774568,
            155576970220531065681649693,
            251728825683549488150424261,
            407305795904080553832073954,
            659034621587630041982498215,
            1066340417491710595814572169,
            1725375039079340637797070384,
            2791715456571051233611642553,
            4517090495650391871408712937,
            7308805952221443105020355490,
            11825896447871834976429068427,
            19134702400093278081449423917,
            30960598847965113057878492344,
            50095301248058391139327916261,
            81055900096023504197206408605,
            131151201344081895336534324866,
            212207101440105399533740733471,
            343358302784187294870275058337,
            555565404224292694404015791808,
            898923707008479989274290850145,
            1454489111232772683678306641953,
            2353412818241252672952597492098,
            3807901929474025356630904134051,
            6161314747715278029583501626149,
            9969216677189303386214405760200,
            16130531424904581415797907386349,
            26099748102093884802012313146549,
            42230279526998466217810220532898,
            68330027629092351019822533679447,
            110560307156090817237632754212345,
            178890334785183168257455287891792,
            289450641941273985495088042104137,
            468340976726457153752543329995929,
            757791618667731139247631372100066,
            1226132595394188293000174702095995,
            1983924214061919432247806074196061,
            3210056809456107725247980776292056,
            5193981023518027157495786850488117,
            8404037832974134882743767626780173,
            13598018856492162040239554477268290,
            22002056689466296922983322104048463,
            35600075545958458963222876581316753,
            57602132235424755886206198685365216,
            93202207781383214849429075266681969,
            150804340016807970735635273952047185,
            244006547798191185585064349218729154,
            394810887814999156320699623170776339,
            638817435613190341905763972389505493,
            1033628323428189498226463595560281832,
            1672445759041379840132227567949787325,
            2706074082469569338358691163510069157,
            4378519841510949178490918731459856482,
            7084593923980518516849609894969925639,
            11463113765491467695340528626429782121,
            18547707689471986212190138521399707760,
            30010821454963453907530667147829489881,
            48558529144435440119720805669229197641,
            78569350599398894027251472817058687522,
            127127879743834334146972278486287885163,
            205697230343233228174223751303346572685,
            332825110087067562321196029789634457848,
            538522340430300790495419781092981030533,
            871347450517368352816615810882615488381,
            1409869790947669143312035591975596518914,
            2281217241465037496128651402858212007295,
            3691087032412706639440686994833808526209,
            5972304273877744135569338397692020533504,
            9663391306290450775010025392525829059713,
            15635695580168194910579363790217849593217,
            25299086886458645685589389182743678652930,
            40934782466626840596168752972961528246147,
            66233869353085486281758142155705206899077,
            107168651819712326877926895128666735145224,
            173402521172797813159685037284371942044301,
            280571172992510140037611932413038677189525,
            453973694165307953197296969697410619233826,
            734544867157818093234908902110449296423351,
            1188518561323126046432205871807859915657177,
            1923063428480944139667114773918309212080528,
            3111581989804070186099320645726169127737705,
            5034645418285014325766435419644478339818233,
            8146227408089084511865756065370647467555938,
            13180872826374098837632191485015125807374171,
            21327100234463183349497947550385773274930109,
            34507973060837282187130139035400899082304280,
            55835073295300465536628086585786672357234389,
            90343046356137747723758225621187571439538669,
            146178119651438213260386312206974243796773058,
            236521166007575960984144537828161815236311727,
            382699285659014174244530850035136059033084785,
            619220451666590135228675387863297874269396512,
            1001919737325604309473206237898433933302481297,
            1621140188992194444701881625761731807571877809,
            2623059926317798754175087863660165740874359106,
            4244200115309993198876969489421897548446236915,
            6867260041627791953052057353082063289320596021,
            11111460156937785151929026842503960837766832936,
            17978720198565577104981084195586024127087428957,
            29090180355503362256910111038089984964854261893,
            47068900554068939361891195233676009091941690850,
            76159080909572301618801306271765994056795952743,
            123227981463641240980692501505442003148737643593,
            199387062373213542599493807777207997205533596336,
            322615043836854783580186309282650000354271239929,
            522002106210068326179680117059857997559804836265,
            844617150046923109759866426342507997914076076194,
            1366619256256991435939546543402365995473880912459,
            2211236406303914545699412969744873993387956988653,
            3577855662560905981638959513147239988861837901112,
            5789092068864820527338372482892113982249794889765,
            9366947731425726508977331996039353971111632790877,
            15156039800290547036315704478931467953361427680642,
            24522987531716273545293036474970821924473060471519,
            39679027332006820581608740953902289877834488152161,
            64202014863723094126901777428873111802307548623680,
            103881042195729914708510518382775401680142036775841,
            168083057059453008835412295811648513482449585399521,
            271964099255182923543922814194423915162591622175362,
            440047156314635932379335110006072428645041207574883,
            712011255569818855923257924200496343807632829750245,
            1152058411884454788302593034206568772452674037325128,
            1864069667454273644225850958407065116260306867075373,
            3016128079338728432528443992613633888712980904400501,
            4880197746793002076754294951020699004973287771475874,
            7896325826131730509282738943634332893686268675876375,
            12776523572924732586037033894655031898659556447352249,
            20672849399056463095319772838289364792345825123228624,
            33449372971981195681356806732944396691005381570580873,
            54122222371037658776676579571233761483351206693809497,
            87571595343018854458033386304178158174356588264390370,
            141693817714056513234709965875411919657707794958199867,
            229265413057075367692743352179590077832064383222590237,
            370959230771131880927453318055001997489772178180790104,
            600224643828207248620196670234592075321836561403380341,
            971183874599339129547649988289594072811608739584170445,
            1571408518427546378167846658524186148133445300987550786,
            2542592393026885507715496646813780220945054040571721231,
            4114000911454431885883343305337966369078499341559272017,
            6656593304481317393598839952151746590023553382130993248,
            10770594215935749279482183257489712959102052723690265265,
            17427187520417066673081023209641459549125606105821258513,
            28197781736352815952563206467131172508227658829511523778,
            45624969256769882625644229676772632057353264935332782291,
            73822750993122698578207436143903804565580923764844306069,
            119447720249892581203851665820676436622934188700177088360,
            193270471243015279782059101964580241188515112465021394429,
            312718191492907860985910767785256677811449301165198482789,
            505988662735923140767969869749836918999964413630219877218,
            818706854228831001753880637535093596811413714795418360007,
            1324695516964754142521850507284930515811378128425638237225,
            2143402371193585144275731144820024112622791843221056597232,
            3468097888158339286797581652104954628434169971646694834457,
            5611500259351924431073312796924978741056961814867751431689,
            9079598147510263717870894449029933369491131786514446266146,
            14691098406862188148944207245954912110548093601382197697835,
            23770696554372451866815101694984845480039225387896643963981,
            38461794961234640015759308940939757590587318989278841661816,
            62232491515607091882574410635924603070626544377175485625797,
            100694286476841731898333719576864360661213863366454327287613,
            162926777992448823780908130212788963731840407743629812913410,
            263621064469290555679241849789653324393054271110084140201023,
            426547842461739379460149980002442288124894678853713953114433,
            690168906931029935139391829792095612517948949963798093315456,
            1116716749392769314599541809794537900642843628817512046429889,
            1806885656323799249738933639586633513160792578781310139745345,
            2923602405716568564338475449381171413803636207598822186175234,
            4730488062040367814077409088967804926964428786380132325920579,
            7654090467756936378415884538348976340768064993978954512095813,
            12384578529797304192493293627316781267732493780359086838016392,
            20038668997554240570909178165665757608500558774338041350112205,
            32423247527351544763402471792982538876233052554697128188128597,
            52461916524905785334311649958648296484733611329035169538240802,
            84885164052257330097714121751630835360966663883732297726369399,
            137347080577163115432025771710279131845700275212767467264610201,
            222232244629420445529739893461909967206666939096499764990979600
        ]

    def test_generate(self):
        generated_301_fibs = [fib for _, fib in zip(
            range(301), fibs.generate())]

        self.assertEqual(generated_301_fibs, self.first_301_fibs)


if __name__ == '__main__':
    unittest.main()
