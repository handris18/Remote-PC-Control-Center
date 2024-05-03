from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'remote_pc_controller'
app.config['JWT_SECRET_KEY'] = 'Aminebk2001'  
jwt = JWTManager(app)
mysql = MySQL(app)

users = {
    1: {'user_id': 1, 'email': 'user1@example.com', 'password': 'password1'},
    2: {'user_id': 2, 'email': 'user2@example.com', 'password': 'password2'}
}
# User class
class User:
    def __init__(self, user_id, email, password):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.jwt_token = None

# Route to get all the users data from the database
@app.route('/data', methods=['GET'])
def get_data():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM users''')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

# Sample database to store coding scripts
coding_scripts = [
    {
        "id": 1,
        "content": "7xBkLR7x0XJaydicAZG9d2JaE2XS.K 7PE8Wo 4GotF9WJpLq9CBMz?cs bxWh5Xsd1EoAUkGv7!tDCbKTvb 606Hwc6rcff73hLGk6bgu GA8pT7ePJtGwGMxmkZnMCplpvXQJ5b31rvG?3oL1dhL8uimGWVnv5,jXW"
    },
    {
        "id": 2,
        "content": ".hJ04!oQqBD9ffPi,0Q17REtKS5BSDKjC!dx5GVikuProdBW?EVWJoi.vqbGVNkOxoq6Run0?dlehBhRoPNrSPgL0N.XgF0u huIGpv7zH8Os!j4eHfSe.ZDSjuLQxjxlnEe bdkmzJEXD5,8RuIC8WSes7mS w8RfZHACpKodt6s.Pa6K"
    },
    {
        "id": 3,
        "content": "bsk!Mi5A O?ZVOG1z1lAMOMQH14qk,!NjY,pOP8aBuvCF6Nc6EMi"
    },
    {
        "id": 4,
        "content": "04LPL4fdPK0FPQcUdDXuG74DUAnfT3rQ81p9Pmt? Sd6YAE?m0s7eEj.D7cmyKkmLxuHx6hlnxqOvRxx8hIRZl.DGVkG1C4FVc41jmHYiaJmaD.t4h5lGa NLCeK x2Rbc88fEEBaf7Sk"
    },
    {
        "id": 5,
        "content": "oUArWH5gg6iaY?pyRCi4663uOSp, KlKX5vMrP Xtp,GjPQ,2oJ41P4GFVVC3hbaQiWAW7gv95Ar!NmT4aW!RlHGA s2V6Jfw4h5d,hDp5HXgz3QWGcn6VbYnlnHfg7XsHg!NsrNcBDneoPXq4"
    },
    {
        "id": 6,
        "content": "Kg,WSNusq!y,dpfLooGGRye6dgMjKf!xlGDyRz.MnELOpc04DWikbRabz5.oGVR,O7HK,qNc2CSY3tXkEyP,9y9kiCXbmit.cLJJdFGuFSQxE6QfyxgaNriCrQ4ODnSpmb?2ISWscHgI1iP5yl4HEAXKnvqSINSIOf,G 7VjS,4TN!tBbulCFX4KR"
    },
    {
        "id": 7,
        "content": "?2zfOtdKuLwy ,UAiHQV.vIbku2nvGmkRlagAaSWgTzedUlN7F7mcn8Fg,WGgeqO4d Flv4ncK!ai.Nke0RQCM!6PFVlw !9s9VF6PRVJuIyFN16ERb1xNrorMMK xc?1qs45AbTvNWGiSdbkT4wMkbklo79Osgu3yYjss5Brit5j"
    },
    {
        "id": 8,
        "content": "qiH!8atvnKiFa7qKhxttsmDmIPDj9u3ehYGEB.kQ!cadjH2aF8UFFSs,0a0vtybz2HZBKFK8 a"
    },
    {
        "id": 9,
        "content": "DhIdOXwNPAaCxrKQwAXcnafAmW,LJY8MxNKMfG7ZXCuwJJNe6U1kuZwNPcCclM.RG!kBcwce2ARWslJYYL"
    },
    {
        "id": 10,
        "content": "GEQGU6tn6B,WodFLkSGhgRUir Cm!FbdGYCp qbAGSHRfjJLSSXuJyl7z4pemXkw6GN!QrjLnyUXWkcRW8Elv 15zMI2NjWFnxhxOBjjhieCd0DBFCAq2r6Z!LamsCypAhpiq.u!fDsU.46BInis4hXRoY90WUS8zzron.?q318g4J.h8sAwH5QGIzT017ymwUn4iF1I"
    },
    {
        "id": 11,
        "content": "68WrYZPSK3AKLFXK39QI2m7Nb.8FB0JsChor4sKYaxxrAVVhWMb Zp f4xEBs"
    },
    {
        "id": 12,
        "content": "6xudDb3kJ!3AGtOQ.MR.A7o2CA,cNTqNAQdQWlHrkvUXJdOoUN0XKeaRIWSp4jBh9?KsElNFuToj9b05ruCBoj15NSoeSf6XKNTo73JMKmcgVbQkWyTdzAF9nLMNK34 mQaHABlOEbmSkSVNKIvi6z6Y crpx"
    },
    {
        "id": 13,
        "content": "ux3KYX7TQRkodI4l4!dVpwJ6O TqeJiHYWBMP?UskFD9PrahA9Bo"
    },
    {
        "id": 14,
        "content": "wPr5vXn1cAFaRUyyaqyiCHUpYNI9juvbTvVAJ!usNdMSRLa3GyGuhKdWbzRUZMDMu.Wg2c8WFEtlEKteiqq9JOlv6TC!QgtNjFJMk!9MU3OBDbx4qJ?JclNmZ 0ar GwJ.4vKU2H9V7UmKY!tD3T "
    },
    {
        "id": 15,
        "content": "Pjx5QYLDqzvWZHt99Jk35fcPZKwjC!T,ptSBhutuq!ykl0HAhcQajirvZLv3owYl3g"
    },
    {
        "id": 16,
        "content": "2PFmNrlMKYqwJpKo3C!y?0DFB5Zr5ALj4SmmMzlvxrTzcjt8ltMqXXhQaeYvi1JRHbpUr771aam xO9Nxzx4Hn.7N,XBUTcdw7upztg5b,wytoAS5KMUl29WAL"
    },
    {
        "id": 17,
        "content": "JzvMuUiJl0PWdYL12daEShT,!BGTDsMWjV!p!8RGcO3amYKs19F7Uopb.Y7S9A,cZGOR.WAH7jxW8Q6jag,3EbgiHZv1h1BrY kzuqqmqVUztl C0wQi7Y2AYRFPB6vU31J88nWLfyr2qaNWyOB8GY0zBs"
    },
    {
        "id": 18,
        "content": "pQNGoo,8F!DWwgrISKMQG0M1pdVbXYh05.kUJhcytJlQjEcbiYzQrFBeGSFxkhoSulZbd7 9WOi,SEuwb.hyo7waVWaqc,4X7pSVdHlWHl tNQitntyVngNPXql6EQlfEzaQqqT.E3bNhOaSzDWbS2WEiiGOB0GtgMeg8Q,h7Wox Nw0?hJyQJypx!HUBzf4fMu zo"
    },
    {
        "id": 19,
        "content": "Wb,hzEJQEd9ZIUHSygmiPMJsnuZmQFHujDjf,Wxfp4UqXPWfHHvCEcYzAID2j4JFKo7ut2yq"
    },
    {
        "id": 20,
        "content": ".Vd7KOZEb0DiSCICcc,usCoHAv9jjmRU6hlturVAC0FS7AMXDhS3Xb1X2nEcknkDBkj7.H0CPIhq"
    },
    {
        "id": 21,
        "content": "WdV?b,0cW31ETUzdZn0YZq hfF zavP?OtElA,ecd9HJpga jq9VmurPBd0c91gYoGheEu8SDiopG.V3m.7rrV?bnK"
    },
    {
        "id": 22,
        "content": "mz3f.OsosbJpRF2kX FATVoaNJiZ4BsR9e09J.2VTaNS?QTDD4fLx!D eIEJPSY 9mCdBDPcef9ZzMt4t8w6KJD"
    },
    {
        "id": 23,
        "content": "9p.Let2.XT52.ZOFH9BRt,1bV!UGT5yV!Q3!,893R3I01Gm9BYErVfTt4ScfLjEcQixvoPCEhZOwUkMAHSU8is8RU!!gYEZbJD7Y9102dg0nBv3CA1W7ziEy?vsVoE8"
    },
    {
        "id": 24,
        "content": "oyVhLHzxd,qlDt4Ny5oohzX!EGl31c3oljmfIx4Km0SItOpLVfAoq1gvXcFn.qgWgkTRZy60KT3Ivys7NoComhS!7QCYYPp2o4rsx9fx2uX8KvdO2XOTWnAzXvCPxx9tKcnutG8YBqi99lwrEj0bHoofB,Nr!40Yjr7yi8xq,C"
    },
    {
        "id": 25,
        "content": "bGJ!Cw9mHtAg7K8v?cPpq?!6CFtBQKl4E0WvA7Obf3ypxUA1t6ppdP U8OTh.oMWrTz309cqpSFDVay5dBd1kPJMDu.sWzK9aCD6y1 tgshf.cXiS?HERppEojZ7B8KFmYZN"
    },
    {
        "id": 26,
        "content": "WunqwexcRaDW4NPcw0txHgGHVkLlXvGszNbaRXFY!lzpRlLWCUiczetGNxH0ujw8"
    },
    {
        "id": 27,
        "content": "ywyIXiK55U8Zg0ORtYiTrGl6SMXd5XDmfrLPSSiyrfrLVCdnDlr0G3kAPw2ObDi!IERUUI2S!a2THoDZFAXst G6.ODCPuD58Knz3LmBgy!LJQFGGpXAYHeYc?dP,WN9Rglo QwoNgAE!E aw7zcUU5aA0dVEzzlgcYmWs4!I1LVPm0LYMxYNSb,n9J7wsDe5hKF"
    },
    {
        "id": 28,
        "content": "u3Aftr.Y,RJkB6W,R5ugMA85!QaysXDNeuDXq5dqcS1OYJBx,I N,Di"
    },
    {
        "id": 29,
        "content": "si1ndxMYuo6HnzhzBpmAgrTLzGfx uLSLQwFkXHiiM7lQfsfgZg82Qr.JlTAt!wY"
    },
    {
        "id": 30,
        "content": "sXV4q2!k6z0gXhIoe24,x 9WvwVvF 6RCvftX mpZOukrePlMA9e Q5DX,8TBiViO7TvOFL5aScYK0cQFndfsrnwWSJ?fJ"
    },
    {
        "id": 31,
        "content": "P7nezNI9ZuasnpU5 MZmOBNZX, RCZpiFAY8oNOK1foEZag1714NZdI6unIfeb,aI,fkBv?AAnEHbF,Rp2KT.GG,Yl.umT8ABgdcu6Ab EVpctluC9fHIlOKb2XOv335RYGet6XTBe!wixXpZ3ns9I!CLPPIhyBJngmg9L.utS6GHzYLc4KBmbBn39rEs"
    },
    {
        "id": 32,
        "content": "59q!qpZWeDV9D0Ks?s3AWQqia0aobl!h3jTb ich.3F790pgMdASxE,ZqwpayFyWnYp9I8B3L9zWnSgyD.RCjB3!jyMBonFNa67hZMe590NhKOUGQSyiO?fdJhWkwZESKYl7YrtIXNCT1vmWuoh0557kwhCZOL"
    },
    {
        "id": 33,
        "content": "Y?j7iZUwPukiFs1xBbjEXCSmDQhTX!PtQzEJ?BWojdlpA3IFN6wOTyrdhZyam"
    },
    {
        "id": 34,
        "content": "eaNlttk8QhK.cygk9LIKXpAHiCeWr8S3.a7ApW1vhKaL7HXPdmTzb2WkCch2A4VYn?6paonlOTQhPL,.KacMtsC?wr9!P1IXmm5fiPVHsSUB2?vrUMozvRb.HIGteAkk Cynp.hYE!VCYMU.j1kMdzIugMFdR.DdIhuTn3I41G4"
    },
    {
        "id": 35,
        "content": "iVKgysib2gDAZAajj6n!dnG8g8 .e.N PUno2MrJSNQqitb.XRX9UbPgSJKMRRUybIVzq2?0aG2a7Cmu.CU1hiymND23!uzJ.dCUSinnK4.VqxJ2JxcK3F.Dm wPAMpNYMiLg4CgUppbgTUhOx,"
    },
    {
        "id": 36,
        "content": "J.NiDv3Xv2d5ovkX yLpCOdLfZz4ls5C83DfLAE3eW3L3VgGdrMOmlQF 3kXz1Kc,BCBVH1PoYTlD0F"
    },
    {
        "id": 37,
        "content": "sNlpQzypFlEaP5WbTs7un4BnAMoGW9ud2JtO.,IUiVq3g2Epk0jTatqmG8KLUKbz?ejlzh7 4.5"
    },
    {
        "id": 38,
        "content": "8woQFnOoQSg 0uWb10AQVoH5,zgWhPNEFSMQapJRrusCWSwj,wSNTIhlErT0?KEEp2sKH7G 2 tG!8G?pnEDhX,K rd8HPxBk4wKsjYUmJby ONM2d"
    },
    {
        "id": 39,
        "content": "7znQcqLt8aM?,jJPl7FFHCL0 bfMYD0SRIQmQD2WQFbBg0MWdw"
    },
    {
        "id": 40,
        "content": "SIzS6kakeufbFLTCHR6sicbYeNVi0DH!NTM5j88qZwYnOX gXJPNlkYdof3Xd7USyu5?RDsMCOuQMsWdDkVJxBuCZ1jld"
    },
    {
        "id": 41,
        "content": "MUrrHVqOmxGVsYuz3Jblw fuaSJi.zPi8hssC8cGWStGFLBQ M59DGarYvLMAoK?JJbLZ PS!O00t d9d!ESAAq?HhvZpmoWAY8b4XgUVQLY,EXz?WizPj8TR5"
    },
    {
        "id": 42,
        "content": "MiS?7ZK?77dhpJ0MGaxnt9WyhwyeRF2P91W?zUbPT91ISWXs,uuVROdny4IXIJ07V.L jeu7.EnwcxuqtAeKXpiHBHFncoJ QaD.OYEh2TRRbvJO5!ogj1WaSQLfxsMBT?,q"
    },
    {
        "id": 43,
        "content": "jpaXdKSaPWNAJxhu3dPde7RcysomXHEiCuqOufmBeTkxf,M8To 7wFBG0.Z8rl1c94dcwcezmvDV9O8j249ur2 yKs0j!53n0OSG6AVHc4LDVz3LvnyZZvEurE0lFBxp0e.xmID8G3kI18suELikrvrcSDjYv8u?IqzISTsErXKI5TVunEnbuv2NGG8N"
    },
    {
        "id": 44,
        "content": "mfi3H0bqJ4BQRXPYXGr0mUwZCVK0yqeJUbPMiXCDYKDZE9YZ3N74qHEpzY7J8cOTG2Q1oS1TkWifSZIlGD54?Ju"
    },
    {
        "id": 45,
        "content": "y54zpcHV3x2fgTBFH!,u.R4,9NX8QAjyGWjCsB9oVCwFen4Uj?lN8efrjxWy RDAum9Zjr.,e7MeUp,0lSFXOd 7zmIQYke?Cs!we omu"
    },
    {
        "id": 46,
        "content": "39rW2V0DiIiqk5KII0EQeGZrkfwfslvsW86gK1e?pi6QOe4WqbiXg,svbroFSsVMwpqFcBqK!MAG?25HWVFSydud.z1lVzD5ipsC,VrFu0Y0m312HkFjRa7Jp1hJC8u,MOWXwmGhBfaJS9.Fqor3E6pilcCkh!1aQQe.4NFoI.vUV2Q"
    },
    {
        "id": 47,
        "content": "o9ndRi??PKxirfabEji4X8Wb7SbsS3XxF.Tdv,okdSK 8ro23qd2G6vYDkhzX!V2iwn!QeulniUllLiAHsJdMwbL?Q7G2.,cVURQ1JsQFbB"
    },
    {
        "id": 48,
        "content": "bg .BUkMU5pxuC68TfAYa?KZgGdDv?zhs0Ow7Ix8UFpLqdzk2qVwDHDJWf1EbTe0w83qLwsGi07x,8R0?7c?0k"
    },
    {
        "id": 49,
        "content": "EHWseTLb255tdhMddG3gM8awRZI40YC8KYP 6SuTiz?wfxu?lFy6bxFklwwJ?cwvnLUZFfN!Y7qr qYRT0tXG7QvcpNQi0bhMklVzipix6MyHxAuNhOYOw9uiSc"
    },
    {
        "id": 50,
        "content": " 6gh2xK3qDRWKbh4eIu2PSiZYteD!LgmVzz9qCi81CTq zoswlzZ2fymkS7NnJVna!I5YVv5SkCzLgbSGlG 77NC1Ly0 4m0pE6lZkae.zQAol.U4k3E23r1rCh hvP8P0c2JRl7NlHEmnm1,Yrz0.j7sJkR3E,24ouDJ,eY2t7HDUCta33vWUsxSL3"
    },
    {
        "id": 51,
        "content": "sYXz8zZScWDJW578YO0Jrg,c ?kxP ? vBFcLdRqD.tL.8X.RWBdvrQD,7FuRo7OwEpUP8ZBLnhR141v.fecqk8dTbWdeP 6R"
    },
    {
        "id": 52,
        "content": "sWG2TwFLVf7xMOi7WGSDin6Iw,qD3tUCHwYK?lQ4fL.YmmuPwc9dvu8cTyR4fyLgt 3JXfvvAb3 SGxU5odgkRE1oSofswdhuPD1n!U1r?xWKRnfvy6U n6TyyNinGLv!mTt7aqEn FoAUvWk!INJ2mxSV!U2Zk?jYvYaP61GP5NryOVxavJX"
    },
    {
        "id": 53,
        "content": "FGICk5OIe9?AQG8wdU5A9FJx!,SYoPtXqPsPD5ok!enieWQ6QKCYPmdl8UEXKl AmKbT6F?UtyYo0ABwG8qlapWdjoXCV1RCK!gxBPl2Km2tfOV,Z1zrWyW7NjPT7,yT?ih961BXWNjvRDh mpzVKzEXD5KPrNwmz"
    },
    {
        "id": 54,
        "content": "gvDJPC1J,puNzQSnoRSzHCkMuEBlksSYxQz15ap1E.d2iuMRKT5Ew3xuMls3wqmX.Ws?Z3bKhp7fp1pSmVwzItpbKE2dR"
    },
    {
        "id": 55,
        "content": "iYyT,RZ S6EoF?1IRif1vuRi.4LAfr!HkMVgUtB,XlbtqhtbYr!MfIyDPNWWrxg,LreMM7PLN4F!4U9LnZefI3d3vrOAtAtUxH5Hin 0u3xnT9eELo0cBr3qhjJFTF5.NsBkoW65N"
    },
    {
        "id": 56,
        "content": "bgUulJQGncdDMC1T1sY1jVcw72psF8zJl.VeJjBgNxjRoK8h0Oiatl2y08I ?p5.Jov!QXCZeNeePRj4.Xvp1?aic 3T alZ?CyqcyQkynWk12OEnVLn1q"
    },
    {
        "id": 57,
        "content": "p?dHA8BpR 6RATMP4PVoMDJYUYkYmlEt1l.fyT rv8,d4vvG?oTKq CypP"
    },
    {
        "id": 58,
        "content": "mgE,e21YJLbY4Twm C6z66zsUrnRyAZc1Yu8h5SGNU6CHvz8NFBCA?cnXLffgn6uamH 7nA3TlmRG2I9MPPwrRn4OsQoHhVpG2u"
    },
    {
        "id": 59,
        "content": "DHfIZpCkOlGQattBOpz7eiV.zzP mkFB17TkixGAnP7tnEK7qAipqenCm UkFogtb43fhwU4P"
    },
    {
        "id": 60,
        "content": "MUY465JQW0n16NHQ4aEJrmQMImT88,2QPhn,w.n kqTxSfuikuYj1HTT6m.bKeu gkexQdTN5VWjkbxvGhXEn!idAl?EFmIse"
    },
    {
        "id": 61,
        "content": "7uQDyBlTnZoDm6ue.3cIkwwf6DOB!azia?UoWPfJQZ9WK.oQl3VII1IRWHBprhOl3lo6bDP3"
    },
    {
        "id": 62,
        "content": "W.JqfQC5VVZ51wrR98o ayw3IMO GFc 4jO2lCfeNkV8b0nTDZXf8lS6pMKdjfOJWLsFPKHQgBxwxAr39cdhdu2KNKUD3f SD89Ri1D2L.VhuCx1UY1sjE.1RSnUcBWUHbPpWleX0RpU0RYmFg?whgQe?Qa6DWv!Mq!UQk54"
    },
    {
        "id": 63,
        "content": "WpfNrfQ1tI6t.4rpprwxPM2J1x2 OPoeeH9kWXnrV5mDdpmxEglkcgn.coijpxN9pif0r2Za Tfx5P.7OFd?umux35w4?4TdPVJn02GY7 4SGc4hCjkhAHhjwnCQP"
    },
    {
        "id": 64,
        "content": "79obJoBzDwUmhoFnoyJV7PnJyJAsmEsr4!gCvkc8mNWZLsuE6,RuC0Lp39vW,WkdWec05jJc?ZDfWhwKKr7Yl!E.tdFDx9OH,PxZCeedO.HcvSkJXIIJBPrUz9Ap2z,tOH34G8f46DG49V0AkF2fh2QcgReeuZ0lzB9K !r!k5lDdNGQvzuA"
    },
    {
        "id": 65,
        "content": "vGqyFnMZqdw6jXyyteA!pcyL1YPOZOMdypLW6D3ptNG6eXS2ZRjfpteMKnv6E,urSMCPSGcNh2zOoopBZ!sOaIsoRJE0MnvE,pSDfGQp?H9wE9W59"
    },
    {
        "id": 66,
        "content": "z8jgNj85WCkzqdtT!FJ4VpPAfTVi3KxIrSt.fJVT3 !ZOwxLdDLfhNom1.z"
    },
    {
        "id": 67,
        "content": "jfxlP5sVUxq,rPcY6wVF04hlIy8Yt?flVn!UuSFhc6DNvqS4yo53KGDnvOrhkWFiq4KZbCFf5rbQba1f.ahNeoIlUuSc!zghRNjiH2IcElbWl,6PD5n!05EKkaisrILCy.vbbfRF.V!yqVRB,Rn6670.!uFQt9YUwdEOzDUK5xQZuPbm500BMmRkL"
    },
    {
        "id": 68,
        "content": ",UlnA!IiE!wOTSRExHyMa.qAJRDiWiS0NFffwCE3v,,PwmmvZOxEgQDNvpggwr!6pSE6Lpsxg5fXTHo9cn4y?4tcy3A1f,S7?Swh7Zunb6wD.HLPrwHiYZPYPx Rh3sYcJUYplMJiFm99kkM5CQQlpuv5bnwh6xsIyS5W8EpVLWapy8oOAOJ5dnM?UTpmIEQxG"
    },
    {
        "id": 69,
        "content": "SR28o6Tt1KFn6Leo0ZXH 9VoSy9ozB53XycPFndcGLRg8f18oghM.ZxPabpD1RGiACBcp?YVZ"
    },
    {
        "id": 70,
        "content": "XQnOeF8900mY36UvHxrfV,p?sbnACbnHcaoQYkEKXVbUFe3KmE954WAzupxh ruAVdp42PvGIR2Vw9?FajS FaVSWNLM4YElDr0YJpZVCked"
    },
    {
        "id": 71,
        "content": "qcUD1hx0CtWZo!M4dh.54uSm7Z1P8h,32 jLlha2l9a oWwlIrG8ZqsDiP1i?JcqmmOZHq C FXNI,a?HorqQJUxgH,iW7,R0I"
    },
    {
        "id": 72,
        "content": "JPdaSq3Ykjfmogyp8G!MEn6x5WjVQIrI.H2nMnaFlsPy?R5Y7sfpRH86iK 3tOIVkxgsReDCQO,!TiW0u5KxRxF.6G!SEHS!?DiMsio5age0 PNKIZN25iy12mNXrmhM gjU1GAWe cB8S3EivT0ZcSo3j3J1e52x r!megYhAlzp44AcpFe h"
    },
    {
        "id": 73,
        "content": "cExZ1oQt9i0sPaL9SPK86Pf,Oq.cWwT4xhodk4qZx1sqQPhn4FvOsq5kRBZtrtNiZQ3ByGKv1msT?lhgJPBDMx4pt,6OVS inOBHtt9VtLEMScJ"
    },
    {
        "id": 74,
        "content": "cmr?C5h1MN4JjB9PHWlTjex uQim,rDePiIlxdfuCTNvq5SeSRgQJ9i6sfW.4j?5giPLLP LpmI2y3.8xWz99YcJJYe!VeA60pbzh"
    },
    {
        "id": 75,
        "content": "kxbZPb1rR2oDD8R8Ty7e6tWwwKJc46NNjasmFUsfHOL az4OkeKHGdlAE?Np!rLKZDcvcMx FF Jd,cr"
    },
    {
        "id": 76,
        "content": "4FpyuhdAwVN3Z7 7ULZGBNLVMMB3bafCm!TE7zS7WW202E7X3PY3qH!pJMhVucWywKxZlHcLufizDlj8?WQ.nl!GmGdB8Uay,r.SoeKG1l,msj?!TsJGWZp5nlVIS"
    },
    {
        "id": 77,
        "content": "11VYkwGpNkC0MPZynojaCyKryC8ADEZDm z9MWlybOaKhh,nyhwq00sS8cntLn5!6R337th.B,aIy.IboQ 4l5f"
    },
    {
        "id": 78,
        "content": "?4Qc!lzLCIO5Mf?DS6vTFnBeGvEhkde8hr8UMU3VbdUg1OQAdzB7b5bbkVSNJGyuXZPsHw5FM8qEU"
    },
    {
        "id": 79,
        "content": "wbN5FfMq.wQz35LGNypYPuri2V5D2vUoPMHITEiL d3VFXzbg8OCZkAI!iPHSK ?mUJQVX9El7xBgbgeZGb"
    },
    {
        "id": 80,
        "content": "JPG9bezv,waJSJcVdY1HXmAhYDT7.W hZMOq10dWv OHHJqpKJxdlvucfH0unriHQflfvENBzjVbD4RaYvi0vw40076zMAGBTj?XSNnixfXfSdPJvYQOa4?lZZI6oI3QY5RUpP2Ba,.fhI5uX0ytS40!LivDt9WsEskoWnWWIRACXDyLqBhJ,H2v"
    },
    {
        "id": 81,
        "content": "kvCDD,sA2D,ZSpZLXdo5dJJAk3xGpGTFWmuBOqTYYS,gyAVhPsUrL.RjIB1!R!L8RD3x!HgdAuTMYAgHGwr8ZB1650z5WFuiI.cxNa3nq6ogiJAsqwe,"
    },
    {
        "id": 82,
        "content": "YQO?ykXQFW6e,hGSfStAKP1eK95rjUPhfiN !NC24HLeOPYHLhv2NzkbVvK"
    },
    {
        "id": 83,
        "content": "yISHTgshyfuHGGOCf.8WXXMzaoK5rK lEMPi2wD.yCRG9iRf4r6m9ppfK1ngkPH19fna0K?mprPTaNq KZGA3xfb,z38zmST24noy,fJ0aiqm2i6xt2Z31CSY?pO eZmombz!coHTKckwQ5ne"
    },
    {
        "id": 84,
        "content": "!rc.O9YpQ2QmS9sj6RbS,,Clj5o5FH8mAPd2MekvCtR gFqA!A8rfOoI1aBvoxOg3MU9XtCTus,HKYiyxovo?VlvjddD6OSAgD3FtZFBb8xxds5GS9N7t7p!IR1J!i4Lfy"
    },
    {
        "id": 85,
        "content": ",D,XW3Hta!Rr4NTq4ITh.3ebFD6rh0RgI3W6Qq JjNUD1VE?OU51zx?o6B6CiHVvhYa!C6JXXn Q7T sMUKCDoWOf8jb5D5ivxk9JeAB69KPAIMMsKqYZecemtX2"
    },
    {
        "id": 86,
        "content": "Ma7A1PmGZlHK4MF5EhvJmSoXR2gcUoaDNTchEsg17cu XCVmTpf2Y.zpToupTkJKpr?jV0S3dLCFktoXfIO7nFxVQYgcXZxNINaY2rj27J4 dNwHtvUGfZq?pk7,?bRV.Zmvlgf8EX,n?c"
    },
    {
        "id": 87,
        "content": "ByAzd!QqaP,6Rql!wxYcYiabxZZtdy!RyY!IzTfaT3nug,YBVgF19IR2HElk604U4RZdOxRcMR18AF9?FAvFR6hrkZVn6CKZBsxREatZiP!D!9qs!WAQsKX.bpeKoo!0KMU3QD!llLGR7m5p!!c0JA5Y7G4tXKtjgQ,Yd!258u8cINnk"
    },
    {
        "id": 88,
        "content": "mJo8rUwCxa8t?yHyC7Te9.C!sIYZe9soHYO3aQIiL1v!q2WFuXdWyiUmJ4vSv 3Q!J2poxzehT9LyRlxdxnlk!N36aONfNCD"
    },
    {
        "id": 89,
        "content": "xNrkzJ7C.MdEua7OFyL40iC6CewS24TKClAcniln0uu1K?r eqb9vYnqW3xW208lvPx9.T2jIOnbAlG3s0QoaZoc2TjJ1yBqBKkRg6N8tM2 bg9a 0k .4l0N02ASm2M.kSvfiqAgDjpQPUQTlxG!Kx?P0YmvsM.aEHRv8kVMXYkBfW2ZVvLAvby!.Qu6hcdr6GtN"
    }
]

# Endpoint for user login and JWT token generation
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user_id = data.get('user_id')
    email = data.get('email')
    password = data.get('password')

    # Check if the provided user_id exists in the 'users' dictionary
    if user_id in users:
        user = users[user_id]

        # Check if the password and email matches
        if user['password'] == password and user['email'] == email:
            # Generate JWT token
            access_token = create_access_token(identity=user_id)
            return jsonify({'message': 'Login successful', 'access_token': access_token}), 200

    # Return error message for invalid credentials
    return jsonify({'error': 'Invalid user ID , email or  password'}), 401

# Endpoint to create a new coding script
@app.route('/scripts/create', methods=['POST'])
@jwt_required()
def create_script():
    data = request.json
    content = data.get('content')
    if content:
        script_id = len(coding_scripts) + 1
        new_script = {'id': script_id, 'content': content}
        coding_scripts.append(new_script)
        return jsonify({'message': 'Script created successfully', 'id': script_id}), 201
    return jsonify({'error': 'Content is required'}), 400

# Endpoint to fetch all coding scripts
@app.route('/scripts/fetch', methods=['GET'])
@jwt_required()
def fetch_scripts():
    return jsonify(coding_scripts)

# Endpoint to fetch a specific coding script by ID
@app.route('/scripts/<int:script_id>', methods=['GET'])
@jwt_required()
def fetch_script(script_id):
    script = next((script for script in coding_scripts if script['id'] == script_id), None)
    if script:
        return jsonify(script)
    else:
        return jsonify({'error': 'Script not found'}), 404
    


# Endpoint to execute a specific coding script by ID
@app.route('/scripts/<int:script_id>/execute', methods=['POST'])
@jwt_required()
def execute_script(script_id):
    script = next((script for script in coding_scripts if script['id'] == script_id), None)
    if script:
        # Execute the script here (this is just a placeholder)
        return jsonify({'message': f'Script {script_id} executed successfully'}), 200
    else:
        return jsonify({'error': 'Script not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
