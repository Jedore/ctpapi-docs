<p>订阅私有流。该方法要在Init 方法前调用。若不调用则不会收到私有流的数据。推荐使用THOST<em>TERT</em>RESTART方式订阅私有流。</p>
<span class="anchor" id="8b5e89b2-710a-4cc8-b673-d8c2235f10ee"></span>
## 1.函数原型
<p>virtual void SubscribePrivateTopic(THOST<em>TE</em>RESUME_TYPE nResumeType) = 0;</p>
<span class="anchor" id="3e22dd89-c9c1-41a5-b9e6-2e31e68f9368"></span>
## 2.参数
<p>nResumeType： 私有流重传方式</p>
<blockquote>
<p>THOST_TERT_RESTART:从本交易日开始重传（推荐）</p>
<p>THOST_TERT_RESUME:从上次收到的续传</p>
<blockquote>
<p>序号保存在本地流水文件里，若遇到CTP交易系统清流重启，如果此时不删除原流水文件并继续用RESUME模式接入，则可能收不到私有流回报</p>
</blockquote>
<p>THOST_TERT_QUICK:只传送登录后私有流的内容</p>
</blockquote>
<span class="anchor" id="640e001a-4a83-4c42-8db0-c7110d2070c3"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="90a3f80c-945b-42af-890f-b65b0b31b4e2"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_RESTART);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_RESTART);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="b5e8ba77-f398-4416-b5df-9337ba5b3647"></span>
## 5.FAQ
<p>无</p>
