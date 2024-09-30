<p>请求RULE跨品种抵扣参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRULEINTERPARAMETER/">ReqQryRULEInterParameter</a>后，该方法被调用。</p>
<span class="anchor" id="83d158ec-ddc5-426d-9f3f-8cf9f5880357"></span>
## 1.函数原型
<p>virtual void OnRspQryRULEInterParameter(CThostFtdcRULEInterParameterField *pRULEInterParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="ec32042e-a2a8-4383-87ed-f2f79926cd53"></span>
## 2.参数
<p>pRULEInterParameter：RULE跨品种抵扣参数</p>
<pre><code>struct CThostFtdcRULEInterParameterField
{
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///优先级
    TThostFtdcSpreadIdType  SpreadId;
    ///品种间对锁仓费率折扣比例
    TThostFtdcRatioType InterRate;
    ///第一腿构成品种
    TThostFtdcInstrumentIDType  Leg1ProdFamilyCode;
    ///第二腿构成品种
    TThostFtdcInstrumentIDType  Leg2ProdFamilyCode;
    ///腿1比例系数
    TThostFtdcCommonIntType Leg1PropFactor;
    ///腿2比例系数
    TThostFtdcCommonIntType Leg2PropFactor;
    ///商品群号
    TThostFtdcCommodityGroupIDType  CommodityGroupID;
    ///商品群名称
    TThostFtdcInstrumentNameType    CommodityGroupName;
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
<span class="anchor" id="6ce17b9a-a9ef-44b2-93a2-fc582be76ee1"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="bff1925f-a610-4faa-9c82-a382bbb5a562"></span>
## 4.FAQ
<p>无</p>
