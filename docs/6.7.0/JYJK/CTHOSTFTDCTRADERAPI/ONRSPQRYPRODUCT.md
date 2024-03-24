<p>请求查询产品响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYPRODUCT/">ReqQryProduct</a>后，该方法被调用。</p>
<span class="anchor" id="cc62072b-3638-4be3-aa57-5b49e04ea71f"></span>
## 1.函数原型
<p>virtual void OnRspQryProduct(CThostFtdcProductField *pProduct, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="71a64cf7-7de7-47b2-a24d-52e4801f43e5"></span>
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
<span class="anchor" id="c4af6b53-b9e6-4820-81df-6139c5377b66"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="bd8fdf60-fc0b-4ca5-ab16-aa5ef426879c"></span>
## 4.FAQ
<p>无</p>
