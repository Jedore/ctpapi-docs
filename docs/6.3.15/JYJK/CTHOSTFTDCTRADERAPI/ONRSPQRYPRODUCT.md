<p>请求查询产品响应，当执行ReqQryProduct后，该方法被调用。</p>
<span class="anchor" id="c2897cdb-7e55-4ea5-b0d0-7e00b61ba8f7"></span>
## 1.函数原型
<p>virtual void OnRspQryProduct(CThostFtdcProductField *pProduct, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="de9b8193-0d41-4ea3-b8ef-5d474d4f7437"></span>
## 2.参数
<p>pProduct：产品</p>
<pre><code>struct CThostFtdcProductField
{
    ///产品代码
    TThostFtdcInstrumentIDType ProductID;
    ///产品名称
    TThostFtdcProductNameType ProductName;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///产品类型
    TThostFtdcProductClassType ProductClass;
    ///合约数量乘数
    TThostFtdcVolumeMultipleType VolumeMultiple;
    ///最小变动价位
    TThostFtdcPriceType PriceTick;
    ///市价单最大下单量
    TThostFtdcVolumeType MaxMarketOrderVolume;
    ///市价单最小下单量
    TThostFtdcVolumeType MinMarketOrderVolume;
    ///限价单最大下单量
    TThostFtdcVolumeType MaxLimitOrderVolume;
    ///限价单最小下单量
    TThostFtdcVolumeType MinLimitOrderVolume;
    ///持仓类型
    TThostFtdcPositionTypeType PositionType;
    ///持仓日期类型
    TThostFtdcPositionDateTypeType PositionDateType;
    ///平仓处理类型
    TThostFtdcCloseDealTypeType CloseDealType;
    ///交易币种类型
    TThostFtdcCurrencyIDType TradeCurrencyID;
    ///质押资金可用范围
    TThostFtdcMortgageFundUseRangeType MortgageFundUseRange;
    ///交易所产品代码
    TThostFtdcInstrumentIDType ExchangeProductID;
    ///合约基础商品乘数
    TThostFtdcUnderlyingMultipleType UnderlyingMultiple;
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
<span class="anchor" id="2dd8bd23-6405-4c39-90ea-bcd0802bdc7a"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="f76ece21-58a8-40a5-976a-26c7e3fc5571"></span>
## 4.FAQ
<p>无</p>
