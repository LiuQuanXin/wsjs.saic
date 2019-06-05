# wsjs.saic

    中国商标网爬虫 http://wsjs.saic.gov.cn/

# 搜索输入接口
  
    http://wsjs.saic.gov.cn/txnS02.do?locale=zh_CN&y7bRbP=KGmVkacwvRCwvRCwvsBePVJPCInmAXTyzIGmdVdSYt0qqx0

# 网站分析
```
  referer 必须
  cookie 必须

  cookie 信息
    ajax 接口返回的 JSESSIONID，必须要带到下一次请求里面，
    并且绑定访问搜索接口返回的 cookie（FSSBBIl1UgzbN7N80S，__jsluid），
    根据这两cookie，服务器判断返回的加密函数的执行步骤
    MmEwMD和c1K5tw0w6_的加密都依据搜索接口返回的函数，预加载生成的动态参数；
    MmEwMD，c1K5tw0w6_，FSSBBIl1UgzbN7N80T 是有有效期的，最多用2次就必须换



```
