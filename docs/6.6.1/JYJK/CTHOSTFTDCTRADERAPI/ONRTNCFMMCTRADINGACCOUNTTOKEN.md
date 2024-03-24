<p>保证金监控中心用户令牌，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQUERYCFMMCTRADINGACCOUNTTOKEN/">ReqQueryCFMMCTradingAccountToken</a>后并且报出后，收到返回则调用此接口，私有流回报。</p>
<span class="anchor" id="11d0bc93-367c-4c53-81b5-ec5f995a0cde"></span>
## 1.函数原型
<p>virtual void OnRtnCFMMCTradingAccountToken(CThostFtdcCFMMCTradingAccountTokenField *pCFMMCTradingAccountToken) {};</p>
<span class="anchor" id="d9fdad78-dd2f-411e-a651-f7af793db8c9"></span>
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
<span class="anchor" id="ca2ab01d-2a44-445d-872c-0623b0e26e29"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="3bd9ead1-62b9-4723-9db5-142c6e77b09b"></span>
## 4.FAQ
<p>无</p>
