<p>请求RCAMS产品组合信息查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRCAMSCOMBPRODUCTINFO/">ReqQryRCAMSCombProductInfo</a>后，该方法被调用。</p>
<span class="anchor" id="305a07f9-0fee-4ea4-9486-fa6e9c989116"></span>
## 1.函数原型
<p>virtual void <a href="../ONRSPQRYSPBMADDONINTERPARAMETER/">OnRspQrySPBMAddOnInterParameter</a>(CThostFtdcSPBMAddOnInterParameterField *pSPBMAddOnInterParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="1fd61344-27dc-4f7e-8e4d-a5c1cba1f9f1"></span>
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
<span class="anchor" id="932dd479-09be-4a48-8d1e-43922ff5f93a"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="8d260fd6-f083-4dc4-af8b-92e7d15e64af"></span>
## 4.FAQ
<p>无</p>
