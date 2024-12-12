<p>订阅私有流。该方法要在<a href="../../../HQJK/CTHOSTFTDCMDAPI/INIT/">Init</a> 方法前调用。若不调用则默认按照restart模式订阅。推荐使用THOST_TERT_RESTART方式订阅私有流。</p>
<span class="anchor" id="edb273cd-1ee3-47c7-bbe6-db1196d3e32a"></span>
## 1.函数原型
<p>virtual void SubscribePrivateTopic(THOST_TE_RESUME_TYPE nResumeType) = 0;</p>
<span class="anchor" id="75f0fb61-7d69-4529-9e54-d1a9109b6efb"></span>
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
<span class="anchor" id="c940c75c-47c1-48b4-b6be-69167e2cc30e"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="9bcfd22d-f8a0-43ca-bb58-7a0844ababbb"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_RESTART);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_RESTART);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="966abc30-ec7b-4b1e-bcf0-a1b065b2b176"></span>
## 5.FAQ
<p>无</p>
