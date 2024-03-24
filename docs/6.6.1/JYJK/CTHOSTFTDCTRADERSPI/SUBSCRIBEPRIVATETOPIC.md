<p>订阅私有流。该方法要在<a href="../INIT/">Init</a> 方法前调用。若不调用则不会收到私有流的数据。推荐使用THOST<em>TERT</em>RESTART方式订阅私有流。</p>
<span class="anchor" id="2beca9e0-3f8c-49a6-8378-2ee3ee93c524"></span>
## 1.函数原型
<p>virtual void SubscribePrivateTopic(THOST<em>TE</em>RESUME_TYPE nResumeType) = 0;</p>
<span class="anchor" id="9afe079c-6456-4049-83a9-7572467c9057"></span>
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
<span class="anchor" id="ebf3d0c4-d95c-44a9-ae34-0ddf55454566"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="2a8a0582-4a51-45d9-966b-9fb010980dc5"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_RESTART);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_RESTART);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="83b45ca6-007d-482b-827e-84a67c3de062"></span>
## 5.FAQ
<p>无</p>
