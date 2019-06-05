#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

# brand.js 生成的参数
MmEwMD='3Gb5_izfpUs7kZS0SAdR4yDyPalQagT5aipFdeIKDfptakL81J1iWd1sjfqsYS3Ki7crkvajdoGa7AUA6ygh.oDjVHCf4EZBSixtQAaOpcEyXBXt8wWBxukOcthC7iDeKpDPXKAO892zZDIRvWAdm.c7ieKSy1t1f1HxeiAglGMox7ZjItIKLOclM.sQW0euCnATJ5Zq0CuWhrUrj.BlbwUTBfU8SyoibjAYGS4QqfPztmrfnnjb6GIxXajgv3sV42SFG9km1rCPyO3fCUZe5.dWYQCGqPPsSaUX2nFJ567WeReZzbzvkJzc32Fhaj_Z9kQczvZh1LRqDbaWcaQSHWeyZRCHS61_dySatkbHdJgqjRAeW7BTgFzJiWDjF.NiA1RQYcoRx5jevic.Jpjd_eoLThnGs5ze7bQx4qyGd44GERR'
data='5Ea6tbbKKvxGk0NctyvqtdTzVrXVulR7Z5WyZk_6Ty3ZR2._4SegO78gLeOnyixcOabIfx17fJxduZ62foNVgN3VD8zVlKz_qvpxkLK5b8qcb3OEXvkxyd4SVYsZoLSVNeka70k1jiKfcF6G.JrN3JangKP0cLcS_ph_XGLcWc89MJNArppNYuPusfaXazNFSRFuIn21IXAHoGQrazNYrlpGLDwke_a4vq08trXrDAhPtOM0S7zAB__HiLP1PSUYxBTGSu1Fcqwu77pXrNQGukAJ5ovhGuvlplWhKdDHTHDkHwRmlL.0z75i23jzS9R9pmoFzdpUPf0G__bkCqWGQ3ZWQ4SKswM5tQKOy6LFYyVV21zgWW4fxRuxG7UNxOVOoaSfwpBnOrcNusCvbQaphtXXGdVSE45r3_jJdk2Q6TZPHR4vhs36ObdP6HIXEpnTvfXUfGhzWbPGbwnjAx_qWQuCJdLL6.IXB1UPPQW641xkqtpjxFOHPK.Ig2R0Li0wU8t6lW7lYLVVaYP7U8R0JmBsmTYsSpXgTgMAuwMLF1fp.P0DBOseE8VX_OFmby1llizvsp..Prge.EEi5jx7byyj5aQ8adm0f9Pbq_vGjIfWDlNtyL5iWD8g.nRvs_Njm7w1tkzjjqGtbIOOEHsXVV.t0GuHMXMjaAF129bm01yKNuRmdwte0rKAQsreLAHKoPWrHQ_TWCHL.VLFS8x7HLnlQa8bM06zZ8M3ae21wqBD8DNwyCpobFkUDSabRjVzr947DVcL.yI8ntGlHxLTqiI4ep0vNBorJDsIbG_j8ZSPPopzmukcMWDLRH8XWD_1ADdQNOJyhqwvyRvnge.O0OYcSJQDIOJUCemHzf2WElzUKCxAcYj7BdvHI67h_ouVLrb_r5qp.drZDvWtoSSDFGDOvtMTeC2of.Bj4wz1Oae5lMaolsYmCQXwU5SuQBTWiSMkzdLgH0pPYK2sr5Mnf_mb0iO1tQ6wbh1m84vGAG3n5eM2VHSFE3zv1NwdVGpVq11f6vuo_eUCuER_dAWqVi2AkwvhL.VHqhwWRLrsxCh5Ck1g8lyE32Oh_SL_T2Boq'
cookie='UM_distinctid=16b25b88a27a5-0ff1943c77fda6-5a6a7863-13c680-16b25b88a28466; FSSBBIl1UgzbN7N80T=3L0_MDd2aIrLP0OaA3zwFSVekgK3pav_pDk88TJ1vNkiph_Fumqtz6qUhN1U0yt1B9AmPBPX8Hn0J3mVKSjHtHVXT6_0T73fLbQlPEd..zQwaHfgBvWWyx5.IYjlJ_wZVQH9sx_XrWdH55WLfzIUlUlyGXNM5pD6mstCllPz.ZOy8QHhyxfCHi0J3n4h_EzUvkYlrALgwK.KUp_vFimE9ULKq2BtuEG058WDrYckcz_ULE2eEzZ9Jx3ozQzO1ykALVzhkRuNVhC5kNi.A30w7ichqgYVu21eJdwl5eZ923vfDNcTv_TFfpp0DPRntetYU.C06vCUW8QC5X1Ovwyu.zr5lifRsO6bvQ48JEKdi1IgwpA; tmrpToken=BE3B0B83693F8BF8E7E1654207EEF508'

headers = {
    "Origin": "http://wsjs.saic.gov.cn",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "X-Requested-With": "XMLHttpRequest",
    "Host": "wsjs.saic.gov.cn",
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36 Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.2568.103 Safari/537.36",
    "Connection": "keep-alive",
    "Cookie": cookie+"; JSESSIONID=0C15B9C1F35DB93FD421009AA7CBCCBE; FSSBBIl1UgzbN7N80S=_40HC4oLK653VRQM3eD8CvqB_zMsYIFd4gwn4CgUIBiIfyJ8lD1n4QeaHb06jULZ; __jsluid=917da0c59c0c2783c6d5db92db93f3e6; ",
    "Referer": "http://wsjs.saic.gov.cn/txnRead01.do?y7bRbp=qmFg8Ek5ooQybVswy9Deuxwtfiw6cmqsVKm.grWnsVSeOuBcsbylpDZRV_9XMn5LnGVC9FnrmSANVXQAaMf21WJu51zrT.cyhzWyCKSB.B2exgNxHXJFbkNKKc11fq5nytKSrPIkMnI0NsM5N3HdjeZzAr8",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
}

data = {
    'c1K5tw0w6_': data
}
url = 'http://wsjs.saic.gov.cn/txnRead02.ajax?MmEwMD=%s' %MmEwMD
resp = requests.post(url,headers=headers,data=data)
print resp.content
print resp.cookies.items()

