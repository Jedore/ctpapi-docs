<p>请求查询产品响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYPRODUCT/">ReqQryProduct</a>后，该方法被调用。</p>
<span class="anchor" id="2af0915d-0c81-4fe0-9e0d-8b875473fa03"></span>
## 1.函数原型
<p>virtual void OnRspQryProduct(CThostFtdcProductField *pProduct, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="fcaf7215-7d19-4741-99fc-80f14190eb0f"></span>
## 2.参数
<p>pProduct：产品</p>
<pre><code>struct CThostFtdcProductField
{
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///产品名称
    TThostFtdcProductNameType   ProductName;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///产品类型
    TThostFtdcProductClassType  ProductClass;
    ///合约数量乘数
    TThostFtdcVolumeMultipleType    VolumeMultiple;
    ///最小变动价位
    TThostFtdcPriceType PriceTick;
    ///市价单最大下单量
    TThostFtdcVolumeType    MaxMarketOrderVolume;
    ///市价单最小下单量
    TThostFtdcVolumeType    MinMarketOrderVolume;
    ///限价单最大下单量
    TThostFtdcVolumeType    MaxLimitOrderVolume;
    ///限价单最小下单量
    TThostFtdcVolumeType    MinLimitOrderVolume;
    ///持仓类型
    TThostFtdcPositionTypeType  PositionType;
    ///持仓日期类型
    TThostFtdcPositionDateTypeType  PositionDateType;
    ///平仓处理类型
    TThostFtdcCloseDealTypeType CloseDealType;
    ///交易币种类型
    TThostFtdcCurrencyIDType    TradeCurrencyID;
    ///质押资金可用范围
    TThostFtdcMortgageFundUseRangeType  MortgageFundUseRange;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve2;
    ///合约基础商品乘数
    TThostFtdcUnderlyingMultipleType    UnderlyingMultiple;
    ///产品代码
    TThostFtdcInstrumentIDType  ProductID;
    ///交易所产品代码
    TThostFtdcInstrumentIDType  ExchangeProductID;
    ///开仓量限制粒度
    TThostFtdcOpenLimitControlLevelType OpenLimitControlLevel;
    ///报单频率控制粒度
    TThostFtdcOrderFreqControlLevelType OrderFreqControlLevel;
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
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="d7ec3407-fdd6-443d-be7c-3673649ad2cb"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="6928862a-02a2-4622-9630-2444c39550e8"></span>
## 4.FAQ
<p>无</p>
