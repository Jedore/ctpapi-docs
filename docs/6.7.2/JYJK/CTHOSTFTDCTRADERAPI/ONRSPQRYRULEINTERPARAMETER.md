<p>请求RULE跨品种抵扣参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRULEINTERPARAMETER/">ReqQryRULEInterParameter</a>后，该方法被调用。</p>
<span class="anchor" id="cb0eaa1f-83ca-4697-9129-04e297019ba6"></span>
## 1.函数原型
<p>virtual void OnRspQryRULEInterParameter(CThostFtdcRULEInterParameterField *pRULEInterParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="6312c9d0-9244-4b21-b080-2390eefcadcd"></span>
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
<span class="anchor" id="79b180a8-1acc-46cf-923f-a2ba77b167d0"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="a2d51d8d-ce75-4b8d-8267-09c5544db142"></span>
## 4.FAQ
<p>无</p>
