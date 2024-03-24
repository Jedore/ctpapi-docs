<p>保证金监控中心用户令牌，当执行ReqQueryCFMMCTradingAccountToken后并且报出后，收到返回则调用此接口，私有流回报。</p>
<span class="anchor" id="87a36040-2128-42c1-88f5-64e4084f8525"></span>
## 1.函数原型
<p>virtual void OnRtnCFMMCTradingAccountToken(CThostFtdcCFMMCTradingAccountTokenField *pCFMMCTradingAccountToken) {};</p>
<span class="anchor" id="e14d01a8-d94d-438b-876e-61f6537c85ef"></span>
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
<span class="anchor" id="3a6373c0-2cac-42a9-be4a-bed8d7b3fefd"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="fc1c4bf6-b53c-45be-8079-be97eee582a7"></span>
## 4.FAQ
<p>无</p>
