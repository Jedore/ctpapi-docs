<p>订阅私有流。该方法要在<a href="../../../HQJK/CTHOSTFTDCMDAPI/INIT/">Init</a> 方法前调用。若不调用则不会收到私有流的数据。推荐使用THOST<em>TERT</em>RESTART方式订阅私有流。</p>
<span class="anchor" id="4941c903-5d5d-49f0-b366-9591bc6f1a6d"></span>
## 1.函数原型
<p>virtual void SubscribePrivateTopic(THOST<em>TE</em>RESUME_TYPE nResumeType) = 0;</p>
<span class="anchor" id="8ef3307a-03ed-4e14-bd97-08530d3358c6"></span>
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
<span class="anchor" id="d61712b7-d951-451e-b9dc-79e881f37e7c"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="eb5d1a82-4de6-40d9-9968-844f460d6458"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_RESTART);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_RESTART);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="4b3e2aaf-25e8-4714-a550-e57904f084c8"></span>
## 5.FAQ
<p>无</p>
