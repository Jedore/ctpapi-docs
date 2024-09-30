<p>保证金监控中心用户令牌，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQUERYCFMMCTRADINGACCOUNTTOKEN/">ReqQueryCFMMCTradingAccountToken</a>后并且报出后，收到返回则调用此接口，私有流回报。</p>
<span class="anchor" id="fc73629a-c838-49b3-8016-6bc390dde2a2"></span>
## 1.函数原型
<p>virtual void OnRtnCFMMCTradingAccountToken(CThostFtdcCFMMCTradingAccountTokenField *pCFMMCTradingAccountToken) {};</p>
<span class="anchor" id="28503abc-0f2f-4900-bae4-6c4a75472871"></span>
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
<span class="anchor" id="e14a7822-7d22-4782-99f4-81e014929e43"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="14a6fce4-3c68-4622-9cb7-f924f531c1c2"></span>
## 4.FAQ
<p>无</p>
