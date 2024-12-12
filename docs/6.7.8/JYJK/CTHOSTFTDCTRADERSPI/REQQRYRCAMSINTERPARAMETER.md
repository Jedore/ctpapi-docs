<p>请求RCAMS跨品种风险折抵参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRCAMSINTERPARAMETER/">OnRspQryRCAMSInterParameter</a></p>
<span class="anchor" id="d1761a70-8921-42d8-b9de-5c5b79c11736"></span>
## 1.函数原型
<p>virtual int ReqQryRCAMSInterParameter(CThostFtdcQryRCAMSInterParameterField *pQryRCAMSInterParameter, int nRequestID) = 0;</p>
<span class="anchor" id="05ba6afb-57d3-4b35-bd62-365f9881798d"></span>
## 2.参数
<p>pQryRCAMSInterParameter：RCAMS跨品种风险折抵参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcProductIDType</td>
<td style="TEXT-ALIGN: left;">ProductGroupID</td>
<td style="TEXT-ALIGN: left;">商品群代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcProductIDType</td>
<td style="TEXT-ALIGN: left;">CombProduct1</td>
<td style="TEXT-ALIGN: left;">产品组合代码1</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcProductIDType</td>
<td style="TEXT-ALIGN: left;">CombProduct2</td>
<td style="TEXT-ALIGN: left;">产品组合代码2</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<span class="anchor" id="c942d434-1c8b-411e-882c-deb155a1b88a"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="cb5e2e52-97a1-4069-b3f0-15e04e76aad2"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="b97616a4-7bd2-4fd1-a4d3-bd12b6bfbfd5"></span>
## 5.FAQ
<p>无</p>
