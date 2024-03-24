<p>订阅私有流。该方法要在<a href="../../../HQJK/CTHOSTFTDCMDAPI/INIT/">Init</a> 方法前调用。若不调用则不会收到私有流的数据。推荐使用THOST<em>TERT</em>RESTART方式订阅私有流。</p>
<span class="anchor" id="97eaf05d-c151-4a17-a5cc-8416d1122990"></span>
## 1.函数原型
<p>virtual void SubscribePrivateTopic(THOST<em>TE</em>RESUME_TYPE nResumeType) = 0;</p>
<span class="anchor" id="22fd1044-b790-40b5-9480-8168b89227f1"></span>
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
<span class="anchor" id="b2334f0c-dc96-486c-9c3a-d6f7d2969c7a"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="f8a74de8-1349-4453-82f8-80288b14bbe0"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_RESTART);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_RESTART);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="9219b256-fc09-4a11-b8d5-2fda01cd1296"></span>
## 5.FAQ
<p>无</p>
