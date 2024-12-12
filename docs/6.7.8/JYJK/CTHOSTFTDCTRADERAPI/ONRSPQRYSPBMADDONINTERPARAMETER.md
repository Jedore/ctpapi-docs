<p>请求SPBM附加跨品种抵扣参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPBMADDONINTERPARAMETER/">ReqQrySPBMAddOnInterParameter</a>后，该方法被调用。</p>
<span class="anchor" id="b2a99c90-c3fe-491c-a1d8-e73004d698ca"></span>
## 1.函数原型
<p>virtual void OnRspQrySPBMAddOnInterParameter(CThostFtdcSPBMAddOnInterParameterField *pSPBMAddOnInterParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="a28c447b-0b6b-4f34-8632-bc7e41e803af"></span>
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
<span class="anchor" id="38deb369-ffd6-424e-b92f-bfe3e235aca1"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="513cf90a-841e-402d-921e-d68444f5d413"></span>
## 4.FAQ
<p>无</p>
