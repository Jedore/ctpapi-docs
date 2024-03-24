<p>获取API的版本信息</p>
<span class="anchor" id="df7de803-2146-49c2-a4a6-30e3fb79d887"></span>
## 1.函数原型
<p>virtual const char * GetApiVersion () = 0;</p>
<span class="anchor" id="b322d705-cd5f-4513-a93f-211bb4979698"></span>
## 2.返回
<p>const char * 返回一个指向版本字符串的指针</p>
<span class="anchor" id="3c41bbb6-3be0-4128-afac-8fc754edf410"></span>
## 3.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
printf("版本号为:%s\n", pUserMdApi-&gt;GetApiVersion());
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
pUserMdApi-&gt;RegisterFront(“tcp://127.0.0.1:41205”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="535cc169-729c-4369-a15c-0526675d56c9"></span>
## 4.FAQ
<p>无</p>
