<p>询价通知，使用<a href="../../CTHOSTFTDCMDAPI/SUBSCRIBEFORQUOTERSP/">SubscribeForQuoteRsp</a>订阅该询价通知。私有流回报。</p>
<span class="anchor" id="6f333534-13a5-4a00-b170-ba76581d6317"></span>
## 1.函数原型
<p>virtual void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp) {};</p>
<span class="anchor" id="672bcb65-8d0f-43dd-baa6-2c4ba6c4bfb1"></span>
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
<span class="anchor" id="2883acf6-7886-4d82-8dd8-590f2718b36f"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="7262e6df-2d1b-477b-9396-40a955558701"></span>
## 4.FAQ
<p>无</p>
