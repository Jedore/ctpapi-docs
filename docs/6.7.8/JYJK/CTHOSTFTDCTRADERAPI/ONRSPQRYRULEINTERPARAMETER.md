<p>请求RULE跨品种抵扣参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRULEINTERPARAMETER/">ReqQryRULEInterParameter</a>后，该方法被调用。</p>
<span class="anchor" id="6523db51-a9d7-4ca2-9d9a-18d193976610"></span>
## 1.函数原型
<p>virtual void OnRspQryRULEInterParameter(CThostFtdcRULEInterParameterField *pRULEInterParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="5cef7278-6daa-4cec-b9f6-9c03af102cfc"></span>
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
<span class="anchor" id="ff32da81-ec19-4fe0-9f03-c2c222579d1a"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="5fae7f48-9436-4f52-9847-8071288b79e6"></span>
## 4.FAQ
<p>无</p>
