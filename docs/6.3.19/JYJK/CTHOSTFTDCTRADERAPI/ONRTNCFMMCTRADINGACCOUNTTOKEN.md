<p>保证金监控中心用户令牌，当执行ReqQueryCFMMCTradingAccountToken后并且报出后，收到返回则调用此接口，私有流回报。</p>
<span class="anchor" id="5c56ce28-e7ff-4e5b-9119-c35835a7fbeb"></span>
## 1.函数原型
<p>virtual void OnRtnCFMMCTradingAccountToken(CThostFtdcCFMMCTradingAccountTokenField *pCFMMCTradingAccountToken) {};</p>
<span class="anchor" id="97138b43-efe0-4849-a733-ff532c51bdff"></span>
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
<span class="anchor" id="cea511d3-a905-4ff5-a7eb-adf872496933"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="768e4ce0-e0c0-4a12-b88e-fc7dda4de934"></span>
## 4.FAQ
<p>无</p>
