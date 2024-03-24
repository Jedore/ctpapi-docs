<p>初始化运行环境,只有调用后,接口才开始发起前置的连接请求。</p>
<span class="anchor" id="2821f9b9-699d-42f7-8325-98577d37d319"></span>
## 1.函数原型
<p>virtual void Init() = 0;</p>
<span class="anchor" id="ccc15b5c-2c5e-4427-bb76-3f0eb03624b9"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="61e6df48-de06-4a8d-8a00-a61f37f88122"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="52795644-c635-47e3-ab84-9b8048e4389c"></span>
## 4.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
pUserMdApi-&gt;RegisterFront(“tcp://127.0.0.1:41205”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="cdfa90d2-f5ec-481c-8289-79faa72ad5f0"></span>
## 5.FAQ
<p>无</p>
