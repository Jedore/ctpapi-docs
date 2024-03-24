<p>询价通知，此接口暂时不用，目前使用的是行情的OnRtnForQuoteRsp。</p>
<span class="anchor" id="fe5306a2-c336-49b8-8364-42ef31ab65fb"></span>
## 1.函数原型
<p>virtual void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp) {};</p>
<span class="anchor" id="5ba988da-15e3-430f-9392-fc50e3075bb7"></span>
## 2.参数
<p>pForQuoteRsp：发给做市商的询价请求</p>
<pre><code>struct CThostFtdcForQuoteRspField
{
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///询价编号
    TThostFtdcOrderSysIDType    ForQuoteSysID;
    ///询价时间
    TThostFtdcTimeType  ForQuoteTime;
    ///业务日期
    TThostFtdcDateType  ActionDay;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
};
</code></pre>
<p>ForQuoteSysID：交易所给的一个询价编号，以此定位一笔询价。</p>
<span class="anchor" id="7c3ff0ef-e553-4b7d-9455-cd43fa5897b6"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="479371a2-cbb9-40e1-b335-a310108818c0"></span>
## 4.FAQ
<p>无</p>
