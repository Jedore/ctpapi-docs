<p>保证金监控中心用户令牌，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQUERYCFMMCTRADINGACCOUNTTOKEN/">ReqQueryCFMMCTradingAccountToken</a>后并且报出后，收到返回则调用此接口，私有流回报。</p>
<span class="anchor" id="9f5f230a-b202-43ff-81f8-a540932be7df"></span>
## 1.函数原型
<p>virtual void OnRtnCFMMCTradingAccountToken(CThostFtdcCFMMCTradingAccountTokenField *pCFMMCTradingAccountToken) {};</p>
<span class="anchor" id="d1c83c9b-8294-48b9-a30a-da904850dfd4"></span>
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
<span class="anchor" id="feccfa4f-823e-4cf9-9db3-18ede30a881d"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="72555193-99b6-4cbb-bff4-10414a475d90"></span>
## 4.FAQ
<p>无</p>
