<p>保证金监控中心用户令牌，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQUERYCFMMCTRADINGACCOUNTTOKEN/">ReqQueryCFMMCTradingAccountToken</a>后并且报出后，收到返回则调用此接口，私有流回报。</p>
<span class="anchor" id="4f076584-fec7-437a-bba3-3dfcac699c5a"></span>
## 1.函数原型
<p>virtual void OnRtnCFMMCTradingAccountToken(CThostFtdcCFMMCTradingAccountTokenField *pCFMMCTradingAccountToken) {};</p>
<span class="anchor" id="af168f49-35bf-446c-8085-bc7d2777a42e"></span>
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
<span class="anchor" id="79dcccc7-96f1-4a17-9773-3322b2239266"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="81e8bd27-1311-48a5-81a0-79173015e6fc"></span>
## 4.FAQ
<p>无</p>
