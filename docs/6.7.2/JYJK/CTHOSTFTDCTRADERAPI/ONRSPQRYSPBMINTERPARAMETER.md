<p>请求SPBM跨品种抵扣参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPBMINTERPARAMETER/">ReqQrySPBMInterParameter</a>后，该方法被调用。</p>
<span class="anchor" id="17afcc9a-b5d6-4e89-8e8a-14242e4fd7f1"></span>
## 1.函数原型
<p>virtual void OnRspQrySPBMInterParameter(CThostFtdcSPBMInterParameterField *pSPBMInterParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="90ade74c-528c-4a67-9a20-d7b2ef36ca2a"></span>
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
<span class="anchor" id="710a7aed-0844-4e2e-ab8e-f08bb2a4307d"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="90fe35d4-2006-4c2c-a783-ea0fba79add6"></span>
## 4.FAQ
<p>无</p>
