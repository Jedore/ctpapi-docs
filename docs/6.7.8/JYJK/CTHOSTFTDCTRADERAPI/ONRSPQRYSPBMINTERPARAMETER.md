<p>请求SPBM跨品种抵扣参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPBMINTERPARAMETER/">ReqQrySPBMInterParameter</a>后，该方法被调用。</p>
<span class="anchor" id="acea9fb4-a5c1-4df9-8ae8-c028b5b5e7a0"></span>
## 1.函数原型
<p>virtual void OnRspQrySPBMInterParameter(CThostFtdcSPBMInterParameterField *pSPBMInterParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="116d4937-ea72-465d-8a93-aacde08a0539"></span>
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
<span class="anchor" id="c84e19d6-6886-41cf-bee8-e3ddd4a99c55"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="696f81cc-105b-44c6-b48f-958d75606417"></span>
## 4.FAQ
<p>无</p>
