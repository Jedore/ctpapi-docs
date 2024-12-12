<p>请求RCAMS产品组合信息查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRCAMSCOMBPRODUCTINFO/">ReqQryRCAMSCombProductInfo</a>后，该方法被调用。</p>
<span class="anchor" id="6b6e0870-9b63-4eff-9d28-76b1d6677662"></span>
## 1.函数原型
<p>virtual void <a href="../ONRSPQRYSPBMADDONINTERPARAMETER/">OnRspQrySPBMAddOnInterParameter</a>(CThostFtdcSPBMAddOnInterParameterField *pSPBMAddOnInterParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="5508193b-e3b4-4200-88b8-484a5cb085fc"></span>
## 2.参数
<p>pSPBMAddOnInterParameter：SPBM附加跨品种抵扣参数</p>
<pre><code>struct CThostFtdcSPBMAddOnInterParameterField
{
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///优先级
    TThostFtdcSpreadIdType  SpreadId;
    ///品种间对锁仓附加费率折扣比例
    TThostFtdcRatioType AddOnInterRateZ2;
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
    TThostFtdcErrorIDType   ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType  ErrorMsg;
};
</code></pre>
<span class="anchor" id="4a2ce404-748d-4146-85d4-32f8cd5a6240"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="c3fd6107-96f1-4c2f-bea1-65944ed77c88"></span>
## 4.FAQ
<p>无</p>
