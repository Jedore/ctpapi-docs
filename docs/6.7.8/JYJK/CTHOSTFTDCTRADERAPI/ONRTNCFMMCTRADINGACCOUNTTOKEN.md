<p>保证金监控中心用户令牌，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQUERYCFMMCTRADINGACCOUNTTOKEN/">ReqQueryCFMMCTradingAccountToken</a>后并且报出后，收到返回则调用此接口，私有流回报。</p>
<span class="anchor" id="502b9723-1df8-4995-a4fc-81d24d40084a"></span>
## 1.函数原型
<p>virtual void OnRtnCFMMCTradingAccountToken(CThostFtdcCFMMCTradingAccountTokenField *pCFMMCTradingAccountToken) {};</p>
<span class="anchor" id="0415093b-3122-4c4e-b213-b58615092945"></span>
## 2.参数
<p>pCFMMCTradingAccountToken：监控中心用户令牌</p>
<pre><code>struct CThostFtdcCFMMCTradingAccountTokenField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///经纪公司统一编码
    TThostFtdcParticipantIDType ParticipantID;
    ///投资者帐号
    TThostFtdcAccountIDType AccountID;
    ///密钥编号
    TThostFtdcSequenceNoType KeyID;
    ///动态令牌
    TThostFtdcCFMMCTokenType Token;
};
</code></pre>
<span class="anchor" id="ca3a5d31-5933-45d3-a2e2-61afeca9527f"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="4d1faf6e-adeb-4607-a9c3-0dadce9b7edb"></span>
## 4.FAQ
<p>无</p>
