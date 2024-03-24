<p>初始化运行环境,只有调用后,接口才开始发起前置的连接请求。</p>
<span class="anchor" id="e6976938-e8ee-43ec-86ff-c773633e079f"></span>
## 1.函数原型
<p>virtual void Init() = 0;</p>
<span class="anchor" id="f0acd823-2822-4001-b990-6801d31be125"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="9ddae7a4-e8ed-4962-8c79-3c890d51758a"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="82d51d93-c57f-4fb6-b23b-b4ee712d8fbc"></span>
## 4.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
pUserMdApi-&gt;RegisterFront(“tcp://127.0.0.1:41205”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="b14d76a0-5663-435f-82b4-50e015cebeae"></span>
## 5.FAQ
<p>无</p>
