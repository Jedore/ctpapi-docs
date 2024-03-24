<p>保证金监控中心用户令牌，当执行ReqQueryCFMMCTradingAccountToken后并且报出后，收到返回则调用此接口，私有流回报。</p>
<span class="anchor" id="88cfc1dc-6022-4f98-83b5-8c6be72f5f80"></span>
## 1.函数原型
<p>virtual void OnRtnCFMMCTradingAccountToken(CThostFtdcCFMMCTradingAccountTokenField *pCFMMCTradingAccountToken) {};</p>
<span class="anchor" id="056d63cc-1f5a-4562-8a15-4232459c9c55"></span>
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
<span class="anchor" id="bca42a60-1c3d-4cff-b46f-a25d5b55f973"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="c48d8c82-f968-4180-a300-603269d881d2"></span>
## 4.FAQ
<p>无</p>
