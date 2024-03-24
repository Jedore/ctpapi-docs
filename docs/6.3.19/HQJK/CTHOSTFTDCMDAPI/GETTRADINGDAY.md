<p>获得当前交易日。只有当登陆成功后才会取到正确的值。</p>
<span class="anchor" id="0559fae3-a615-43a5-b3e3-6dfb474c809a"></span>
## 1.函数原型
<p>virtual const char *GetTradingDay() = 0;</p>
<span class="anchor" id="eba5b002-f769-4414-b1ae-afa6f2aaa9c3"></span>
## 2.返回
<p>返回一个指向日期信息字符串的常量指针。</p>
<span class="anchor" id="b9f18245-b2a9-49b1-92f0-6bbdbb7048cb"></span>
## 3.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
pUserMdApi-&gt;RegisterFront(“tcp://127.0.0.1:41213”);
pUserMdApi-&gt;Init();
//登录成功后
printf("获取当前交易日期:%s\n", pUserMdApi-&gt;GetTradingDay());
</code></pre>
<span class="anchor" id="7fb002b2-6a42-4698-bad5-f4f9e1ab327a"></span>
## 4.FAQ
<p><div class="region_i" id=""><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">登录前为什么也可以获取到交易日？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>登录前调用该函数会去上一次的API流水文件里去获取交易日。只有在登录后才能获取到正确的交易日。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
