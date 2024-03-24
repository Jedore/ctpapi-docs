<p>获得当前交易日。只有当登陆成功后才会取到正确的值。</p>
<span class="anchor" id="0577bb88-00d0-413b-b5de-a3ba735d4b04"></span>
## 1.函数原型
<p>virtual const char *<a href="../../../JYJK/CTHOSTFTDCTRADERSPI/GETTRADINGDAY/">GetTradingDay</a>() = 0;</p>
<span class="anchor" id="a61a7966-91ab-4af1-bf15-b5232ea289f5"></span>
## 2.返回
<p>返回一个指向日期信息字符串的常量指针。</p>
<span class="anchor" id="f537d7e5-720f-487b-84f0-926323275a32"></span>
## 3.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
pUserMdApi-&gt;RegisterFront(“tcp://127.0.0.1:41213”);
pUserMdApi-&gt;Init();
//登录成功后
printf("获取当前交易日期:%s\n", pUserMdApi-&gt;GetTradingDay());
</code></pre>
<span class="anchor" id="332ad666-986f-4ce3-b2e8-aa059e074c8d"></span>
## 4.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">登录前为什么也可以获取到交易日？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>登录前调用该函数会去上一次的API流水文件里去获取交易日。只有在登录后才能获取到正确的交易日。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
