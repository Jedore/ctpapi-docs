<p>请求SPBM跨品种抵扣参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPBMINTERPARAMETER/">ReqQrySPBMInterParameter</a>后，该方法被调用。</p>
<span class="anchor" id="32a083b1-aede-45d3-b3c1-b29866ae5406"></span>
## 1.函数原型
<p>virtual void OnRspQrySPBMInterParameter(CThostFtdcSPBMInterParameterField *pSPBMInterParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="b6f0ba80-81e5-43a5-9cdf-d4a6c7116db9"></span>
## 2.参数
<p>pSPBMInterParameter：SPBM跨品种抵扣参数</p>
<pre><code>struct CThostFtdcSPBMInterParameterField
{
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///优先级
    TThostFtdcSpreadIdType  SpreadId;
    ///品种间对锁仓费率折扣比例
    TThostFtdcRatioType InterRateZ;
    ///第一腿构成品种
    TThostFtdcInstrumentIDType  Leg1ProdFamilyCode;
    ///第二腿构成品种
    TThostFtdcInstrumentIDType  Leg2ProdFamilyCode;
};
</code></pre>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<span class="anchor" id="1ede03a0-b0b4-4306-a4ac-8c5e03bc624b"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="7b090832-76ba-4442-8175-c1caac55e024"></span>
## 4.FAQ
<p>无</p>
