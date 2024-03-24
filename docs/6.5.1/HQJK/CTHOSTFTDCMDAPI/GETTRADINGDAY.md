<p>获得当前交易日。只有当登陆成功后才会取到正确的值。</p>
<span class="anchor" id="0506f15c-0b52-4815-9e5b-1dad9054cb86"></span>
## 1.函数原型
<p>virtual const char *GetTradingDay() = 0;</p>
<span class="anchor" id="0728cd83-97a0-40e4-bef6-1e32a9d933ff"></span>
## 2.返回
<p>返回一个指向日期信息字符串的常量指针。</p>
<span class="anchor" id="2fe3042d-d365-47d4-8b89-deb6e51ecb1a"></span>
## 3.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
pUserMdApi-&gt;RegisterFront(“tcp://127.0.0.1:41213”);
pUserMdApi-&gt;Init();
//登录成功后
printf("获取当前交易日期:%s\n", pUserMdApi-&gt;GetTradingDay());
</code></pre>
<span class="anchor" id="0d29080b-7efe-476a-bda3-bbab7d40c62e"></span>
## 4.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">登录前为什么也可以获取到交易日？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>登录前调用该函数会去上一次的API流水文件里去获取交易日。只有在登录后才能获取到正确的交易日。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
