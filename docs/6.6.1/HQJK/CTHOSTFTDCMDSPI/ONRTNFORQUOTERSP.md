<p>询价通知，使用<a href="../../CTHOSTFTDCMDAPI/SUBSCRIBEFORQUOTERSP/">SubscribeForQuoteRsp</a>订阅该询价通知。私有流回报。</p>
<span class="anchor" id="6fc658f2-d31e-4792-91da-c5ef08ae7ce4"></span>
## 1.函数原型
<p>virtual void <a href="../../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNFORQUOTERSP/">OnRtnForQuoteRsp</a>(CThostFtdcForQuoteRspField *pForQuoteRsp) {};</p>
<span class="anchor" id="89fbe763-4252-48b7-b352-9455e761710d"></span>
## 2.参数
<p>pForQuoteRsp：发给做市商的询价请求</p>
<pre><code>struct CThostFtdcForQuoteRspField
{
    ///交易日
    TThostFtdcDateType TradingDay;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///询价编号
    TThostFtdcOrderSysIDType ForQuoteSysID;
    ///询价时间
    TThostFtdcTimeType ForQuoteTime;
    ///业务日期
    TThostFtdcDateType ActionDay;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
};
</code></pre>
<p>ForQuoteSysID：交易所给的一个询价编号，以此定位一笔询价。</p>
<span class="anchor" id="828b841a-5a42-4110-9a00-da4e2a93e30c"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="24d33be4-8b09-4df8-a768-20381b5f53cf"></span>
## 4.FAQ
<p>无</p>
