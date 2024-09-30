<p>请求查询组播合约，对应响应<a href="../../CTHOSTFTDCMDSPI/ONRSPQRYMULTICASTINSTRUMENT/">OnRspQryMulticastInstrument</a></p>
<p>目前只有上期所、原油交易所有组播行情</p>
<p>上期所topicid：1001(一档行情)，1000(五档行情)</p>
<p>原油交易所topicid：5001(一档行情)，5000(五档行情)</p>
<p><strong><font color="#FF0000">注意：该函数只有连接<code>支持交易所组播行情的mdfront</code>才能获得完整功能，连接其他行情前置则不能使用该函数。</font></strong></p>
<p>详细说明见<a href="../../../QTYWGZ/EDHQJR/">二代行情接入</a></p>
<span class="anchor" id="ddaaeaac-738f-4a5e-b026-3028e1f01851"></span>
## 1.函数原型
<p>virtual int ReqQryMulticastInstrument(CThostFtdcQryMulticastInstrumentField *pQryMulticastInstrument, int nRequestID) = 0;</p>
<span class="anchor" id="e9da9e21-0289-4d3b-8fbc-88ce0aba7544"></span>
## 2.参数
<p>QryMulticastInstrument：请求查询组播合约</p>
<pre><code>    struct CThostFtdcQryMulticastInstrumentField
    {
        ///主题号
        TThostFtdcInstallIDType TopicID;
        ///合约代码
        TThostFtdcInstrumentIDType  InstrumentID;
    };
</code></pre>
<p>TopicID：对应交易所组播行情主题号。</p>
<span class="anchor" id="b3e9c7e4-5618-46ee-8380-266f246c885a"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="e6f135bb-717c-46d3-8079-22b6c6c93757"></span>
## 4.调用示例
<pre><code>CThostFtdcQryMulticastInstrumentField a = { 0 };
a.TopicID = 1001;//对应上期所的组播行情topic
//a.TopicID = 5001;//对应原油交易所的组播行情topic
strcpy_s(g_chInstrumentID,"cu1906");
m_pUserMdApi-&gt;ReqQryMulticastInstrument(&amp;a, 1);
</code></pre>
<span class="anchor" id="b24e5dcf-4d98-4b3a-ba24-7385c26a6502"></span>
## 5.FAQ
<p>无</p>
